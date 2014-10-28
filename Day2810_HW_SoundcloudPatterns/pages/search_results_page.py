from Day2810_HW_SoundcloudPatterns.components.search_result_categories import SearchResultCategories


class SearchResultPage:
    _selectors = {
        "categories": "searchOptions__navigation"
    }

    def __init__(self, driver):
        self.driver = driver

    @property
    def categories(self):
        el = self.driver.find_element_by_class_name(self._selectors["categories"])
        return SearchResultCategories(self.driver, el)