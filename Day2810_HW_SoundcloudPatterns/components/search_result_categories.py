from Day2810_HW_SoundcloudPatterns.components.base_component import BaseComponent


class SearchResultCategories(BaseComponent):
    selectors = {
        "everything": "searchOptions__navigationLink",
        "tracks": "searchOptions__navigation-sounds",
        "playlists": "searchOptions__navigation-sets",
        "people": "searchOptions__navigation-people",
        "groups": "searchOptions__navigation-groups"
    }

    def open(self, what):
        self.element.find_element_by_class_name(self.selectors[what]).click()

    def is_everything_displayed(self):
        return self.element.find_element_by_class_name(self.selectors["everything"]).is_displayed()

    def is_tracks_displayed(self):
        return self.element.find_element_by_class_name(self.selectors["tracks"]).is_displayed()

    def is_playlists_displayed(self):
        return self.element.find_element_by_class_name(self.selectors["playlists"]).is_displayed()

    def is_people_displayed(self):
        return self.element.find_element_by_class_name(self.selectors["people"]).is_displayed()

    def is_groups_displayed(self):
        return self.element.find_element_by_class_name(self.selectors["groups"]).is_displayed()