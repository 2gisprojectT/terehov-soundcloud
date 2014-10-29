from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class PlayerBar(BaseComponent):
    _selectors = {
        "title": "playbackTitle__link"
    }

    def title(self):
        title = self.element.find_element_by_class_name(self._selectors["title"])
        return title.text