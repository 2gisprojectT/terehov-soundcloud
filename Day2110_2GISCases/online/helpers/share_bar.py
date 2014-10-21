from Day2110_2GISCases.online.helpers.base_component import BaseComponent

__author__ = 'Alexey'


class ShareBar(BaseComponent):

    selectors = {
        'open_button': '.extras__share',
        'close_button': '.share__popupClose',
        'share_link': '.share__popupUrlInput'
    }

    def open(self):
        self.driver.find_element_by_css_selector(self.selectors['open_button']).click()

    def close(self):
        self.driver.find_element_by_css_selector(self.selectors['close_button']).click()

    @property
    def share_link(self):
        while self.driver.find_element_by_css_selector(self.selectors['share_link']).get_attribute("value") == "":
            pass
        return self.driver.find_element_by_css_selector(self.selectors['share_link']).get_attribute("value")