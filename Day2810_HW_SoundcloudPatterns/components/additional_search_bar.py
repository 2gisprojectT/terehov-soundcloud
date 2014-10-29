from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class AdditionalSearchBar(BaseComponent):
    _selectors = {
        "input": "search__input"
    }

    def text(self):
        return self.element.find_element_by_class_name(self._selectors["input"]).get_attribute('value')