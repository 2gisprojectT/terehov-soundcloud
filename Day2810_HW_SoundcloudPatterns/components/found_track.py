from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class FoundTrack(BaseComponent):
    _selectors = {
        "comment_bar": "commentPopover",
        "comment_input": "commentForm__inputWrapper"
    }

    def show_comment_input(self):
        self.element.find_element_by_class_name(self._selectors["comment_bar"]).click()

    def is_comment_input_displayed(self):
        el = self.element.find_element_by_class_name(self._selectors["comment_input"])
        return el.is_displayed()