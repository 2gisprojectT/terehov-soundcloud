from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class FoundPeople(BaseComponent):
    _selectors = {
        "follow_btn": "sc-button-follow"
    }

    def is_follow_button_displayed(self):
        el = self.element.find_element_by_class_name(self._selectors["follow_btn"])
        return el.is_displayed()