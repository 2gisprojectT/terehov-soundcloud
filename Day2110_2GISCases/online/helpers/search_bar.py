from Day2110_2GISCases.online.helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'mode_transport': '.searchBar__rsTab',
        'transport_from': '.searchBar._mode_rs .searchBar__textfield._from',
        'transport_to': '.searchBar._mode_rs .searchBar__textfield._to',
        'input_class': 'suggest__input'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def search_transport(self, go_from, go_to):
        div_from = self.driver.find_element_by_css_selector(self.selectors['transport_from'])
        div_from.find_element_by_class_name(self.selectors['input_class']).send_keys(go_from)
        div_to = self.driver.find_element_by_css_selector(self.selectors['transport_to'])
        div_to.find_element_by_class_name(self.selectors['input_class']).send_keys(go_to)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def change_mode(self, mode_selector):
        self.driver.find_element_by_css_selector(mode_selector).click()

    @property
    def text(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute("value")