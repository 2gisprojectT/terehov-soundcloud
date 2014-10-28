from selenium.webdriver import ActionChains
from Day2810_HW_SoundcloudPatterns.components.found_track import FoundTrack
from Day2810_HW_SoundcloudPatterns.components.search_result_categories import SearchResultCategories


class SearchResultPage:
    _selectors = {
        "categories": "searchOptions__navigation",
        "result_item": "searchItem"
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