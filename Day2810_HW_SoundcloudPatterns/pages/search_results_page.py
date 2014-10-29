from Day2810_HW_SoundcloudPatterns.components.additional_search_bar import AdditionalSearchBar
from Day2810_HW_SoundcloudPatterns.components.found_people import FoundPeople
from Day2810_HW_SoundcloudPatterns.components.found_track import FoundTrack
from Day2810_HW_SoundcloudPatterns.components.player_bar import PlayerBar
from Day2810_HW_SoundcloudPatterns.components.search_result_categories import SearchResultCategories


class SearchResultPage:
    _selectors = {
        "categories": "searchOptions__navigation",
        "result_item": "searchItem",
        "player_bar": "playControls__wrapper",
        "additional_search": "search__form"
    }

    def __init__(self, driver):
        self.driver = driver

    @property
    def categories(self):
        el = self.driver.find_element_by_class_name(self._selectors["categories"])
        return SearchResultCategories(self.driver, el)

    @property
    def found_tracks(self):
        results = self.driver.find_elements_by_class_name(self._selectors["result_item"])
        objs = []
        for res in results:
            objs += [FoundTrack(self.driver, res)]
        return objs

    @property
    def found_people(self):
        results = self.driver.find_elements_by_class_name(self._selectors["result_item"])
        objs = []
        for res in results:
            objs += [FoundPeople(self.driver, res)]
        return objs

    @property
    def player(self):
        el = self.driver.find_element_by_class_name(self._selectors["player_bar"])
        return PlayerBar(self.driver, el)

    @property
    def additional_search(self):
        el = self.driver.find_element_by_class_name(self._selectors["additional_search"])
        return AdditionalSearchBar(self.driver, el)