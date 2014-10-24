from Day2110_2GISCases.online.helpers.base_component import BaseComponent


class SearchResult(BaseComponent):

    selectors = {
        'self': '.searchResults__list',
        'count': '//*[@id="module-1-9-1-1"]/nav/div[2]/div[2]',
        'no_result': 'noResults__title'
    }

    @property
    def count(self):
        return self.driver.find_element_by_xpath(self.selectors['count']).text

    @property
    def is_empty(self):
        try:
            return self.driver.find_element_by_class_name(self.selectors['no_result']).is_displayed()
        except:
            return False