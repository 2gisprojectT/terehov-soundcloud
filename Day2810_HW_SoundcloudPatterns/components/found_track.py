from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class FoundTrack(BaseComponent):
    _selectors = {
        "comment_bar": "commentPopover",
        "comment_input": "commentForm__inputWrapper",
        "play_btn": "sc-button-play",
        "title": "soundTitle__title"
    }

    def show_comment_input(self):
        self.element.find_element_by_class_name(self._selectors["comment_bar"]).click()

    def play(self):
        self.element.find_element_by_class_name(self._selectors["play_btn"]).click()

    def is_comment_input_displayed(self):
        el = self.element.find_element_by_class_name(self._selectors["comment_input"])
        return el.is_displayed()

    def title(self):
        div = self.element.find_element_by_class_name(self._selectors["title"])
        el = div.find_element_by_xpath('./*')
        return el.text