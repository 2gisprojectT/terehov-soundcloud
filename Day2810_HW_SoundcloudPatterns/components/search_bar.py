from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent
from Day2810_HW_SoundcloudPatterns.pages.search_results_page import SearchResultPage


class SearchBar(BaseComponent):
    _selectors = {
        "input": "headerSearch__input",
        "button": "headerSearch__submit"
    }

    def find(self, text):
        self.element.find_element_by_class_name(self._selectors["input"]).send_keys(text)
        self.element.find_element_by_class_name(self._selectors["button"]).submit()
        return SearchResultPage(self.driver)