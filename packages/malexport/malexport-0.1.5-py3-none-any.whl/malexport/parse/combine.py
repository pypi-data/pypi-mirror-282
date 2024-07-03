"""
A helper module to combine data from the list,
export and history modules into data I find useful
"""

import os
from typing import Dict, List, NamedTuple, Optional, TypeVar, Tuple, Union, Set
from pathlib import Path
from datetime import date

from ..list_type import ListType
from ..log import logger
from ..paths import LocalDir
from .common import split_tags
from .history import History, HistoryEntry, iter_history_from_dir
from .mal_list import (
    AnimeEntry,
    MangaEntry,
    parse_file as parse_user_history,
)
from .api_list import iter_api_list, Entry
from .xml import AnimeXML, MangaXML, parse_xml


T = TypeVar("T")

FILTER_TAGS = "MALEXPORT_COMBINE_FILTER_TAGS"


class AnimeData(NamedTuple):
    XMLData: AnimeXML
    history: List[HistoryEntry]
    JSONList: Optional[AnimeEntry]
    APIList: Optional[Entry]
    username: str

    @property
    def runtime(self) -> Optional[int]:
        """
        Returns the total runtime of the anime in seconds, or None if couldn't be computed
        """
        if (
            self.APIList is None
            or self.XMLData is None
            or self.XMLData.episodes is None
            or self.APIList.average_episode_duration is None
        ):
            return None
        seconds = self.XMLData.episodes * self.APIList.average_episode_duration
        if seconds == 0:
            return None
        return seconds

    @property
    def watched_seconds(self) -> int:
        if (
            self.XMLData is None
            or self.APIList is None
            or self.APIList.average_episode_duration is None
            or self.XMLData.watched_episodes is None
        ):
            return 0
        watched_time = (
            self.XMLData.watched_episodes * self.APIList.average_episode_duration
        )
        # if Ive rewatched, add time for that
        if self.XMLData.times_watched > 0 and self.runtime is not None:
            watched_time += self.XMLData.times_watched * self.runtime
        return watched_time

    @property
    def start_date(self) -> Optional[date]:
        if self.JSONList:
            return self.JSONList.start_date
        return None

    @property
    def finish_date(self) -> Optional[date]:
        if self.JSONList:
            return self.JSONList.finish_date
        return None

    @property
    def id(self) -> int:
        return self.XMLData.id

    @property
    def tags_list(self) -> List[str]:
        if self.JSONList:
            return split_tags(self.JSONList.tags)
        return []


class MangaData(NamedTuple):
    XMLData: MangaXML
    history: List[HistoryEntry]
    JSONList: Optional[MangaEntry]
    APIList: Optional[Entry]
    username: str

    @property
    def id(self) -> int:
        return self.XMLData.id

    @property
    def tags_list(self) -> List[str]:
        if self.JSONList:
            return split_tags(self.JSONList.tags)
        return []

    @property
    def start_date(self) -> Optional[date]:
        if self.JSONList:
            return self.JSONList.start_date
        return None

    @property
    def finish_date(self) -> Optional[date]:
        if self.JSONList:
            return self.JSONList.finish_date
        return None


CombineResults = Tuple[List[AnimeData], List[MangaData]]


def combine(username: str, data_dir: Optional[Path] = None) -> CombineResults:
    if data_dir is None:
        acc = LocalDir.from_username(username)
        data_dir = acc.data_dir

    assert data_dir is not None

    # read history
    history = list(iter_history_from_dir(data_dir))
    anime_history: Dict[int, History] = {}
    manga_history: Dict[int, History] = {}
    for h in history:
        if h.list_type == "anime":
            # should never overwrite stuff by mistake
            assert h.mal_id not in anime_history
            anime_history[h.mal_id] = h
        else:
            assert h.mal_id not in manga_history
            manga_history[h.mal_id] = h

    manual_anime_history: Dict[int, History] = {}
    manual_manga_history: Dict[int, History] = {}

    # read manual history
    manual_history_file = data_dir / "manual_history.yaml"
    if manual_history_file.exists():
        from .history import parse_manual_history

        for h in parse_manual_history(manual_history_file):
            if h.list_type == "anime":
                # make sure groupby worked
                assert h.mal_id not in manual_anime_history
                manual_anime_history[h.mal_id] = h
            else:
                assert h.mal_id not in manual_manga_history
                manual_manga_history[h.mal_id] = h

    # there's a possibility that the JSON exports don't
    # exist, because of private lists
    animelist_json_data: Dict[int, AnimeEntry] = {}
    mangalist_json_data: Dict[int, MangaEntry] = {}
    if (data_dir / "animelist.json").exists():
        animelist_json_data = {
            el.id: el  # type: ignore[union-attr,misc]
            for el in parse_user_history(
                str(data_dir / "animelist.json"), list_type=ListType.ANIME
            )
        }
    if (data_dir / "mangalist.json").exists():
        mangalist_json_data = {
            el.id: el  # type: ignore[union-attr,misc]
            for el in parse_user_history(
                str(data_dir / "mangalist.json"), list_type=ListType.MANGA
            )
        }

    # xml exports should always exist
    animelist_xml_data: Dict[int, AnimeXML] = {
        el.id: el  # type: ignore[union-attr,misc]
        for el in parse_xml(str(data_dir / "animelist.xml")).entries
    }
    mangalist_xml_data: Dict[int, MangaXML] = {
        el.id: el  # type: ignore[union-attr,misc]
        for el in parse_xml(str(data_dir / "mangalist.xml")).entries
    }

    # list using the API
    animelist_api_json_data: Dict[int, Entry] = {}
    mangalist_api_json_data: Dict[int, Entry] = {}
    if (data_dir / "animelist_api.json").exists():
        animelist_api_json_data = {
            el.id: el
            for el in iter_api_list(
                str(data_dir / "animelist_api.json"), list_type=ListType.ANIME
            )
        }
    if (data_dir / "mangalist_api.json").exists():
        mangalist_api_json_data = {
            el.id: el
            for el in iter_api_list(
                str(data_dir / "mangalist_api.json"), list_type=ListType.MANGA
            )
        }

    anime_combined_data: Dict[int, AnimeData] = {}

    # combine anime data
    for mal_id, anime_xml in animelist_xml_data.items():
        anime_hist: List[HistoryEntry] = []
        if mal_id in anime_history:
            anime_hist = anime_history[mal_id].entries
            anime_history.pop(mal_id)  # remove from anime history dict
        if mal_id in manual_anime_history:
            anime_hist += manual_anime_history[mal_id].entries
            manual_anime_history.pop(mal_id)

        anime_hist.sort(key=lambda x: x.at)

        anime_combined_data[mal_id] = AnimeData(
            username=username,
            XMLData=anime_xml,
            history=anime_hist,
            JSONList=animelist_json_data.pop(mal_id, None),
            APIList=animelist_api_json_data.pop(mal_id, None),
        )

    manga_combined_data: Dict[int, MangaData] = {}
    for mal_id, manga_xml in mangalist_xml_data.items():
        manga_hist: List[HistoryEntry] = []
        if mal_id in manga_history:
            manga_hist = manga_history[mal_id].entries
            manga_history.pop(mal_id)  # remove from manga history dict
        if mal_id in manual_manga_history:
            manga_hist += manual_manga_history[mal_id].entries
            manual_manga_history.pop(mal_id)

        manga_hist.sort(key=lambda x: x.at)

        manga_combined_data[mal_id] = MangaData(
            username=username,
            XMLData=manga_xml,
            history=manga_hist,
            JSONList=mangalist_json_data.pop(mal_id, None),
            APIList=mangalist_api_json_data.pop(mal_id, None),
        )

    # while parsing, items were removed when they were merged into
    # the combined data. if anything still exists here, then warn
    if len(animelist_json_data) > 0:
        logger.debug(
            f"animelist_json_data entries left over (likely different parts of export are out of sync or entries on your list were deleted by MAL): {animelist_json_data}"
        )
    if len(mangalist_json_data) > 0:
        logger.debug(
            f"mangalist_json_data entries left over (likely different parts of export are out of sync or entries on your list were deleted by MAL): {mangalist_json_data}"
        )
    # shouldn't be warned for -- if you delete something off your list the
    # local history files still remain -- not sure if the should be deleted
    #
    # if len(anime_history) > 0:
    #    logger.warning(f"anime_history entries left over: {len(anime_history)}")
    # if len(manga_history) > 0:
    #    logger.warning(f"manga_history entries left over: {len(manga_history)}")

    anime_combined = list(anime_combined_data.values())
    manga_combined = list(manga_combined_data.values())

    # e.g. if you had MALEXPORT_COMBINE_FILTER_TAGS="no source,no raws"
    # anything which has those tags would be removed
    # from the results here
    if FILTER_TAGS in os.environ:
        filter_by_tags: List[str] = os.environ[FILTER_TAGS].split(",")

        # if this entry has any tags which are in the filter list
        def filter_func(e: Union[AnimeData, MangaData]) -> bool:
            tags: Set[str] = set(e.tags_list)
            return not any(t in filter_by_tags for t in tags)

        anime_combined = list(filter(filter_func, anime_combined))
        manga_combined = list(filter(filter_func, manga_combined))

    return anime_combined, manga_combined
