from Day2110_2GISCases.online.helpers.base_component import BaseComponent


class RouteResult(BaseComponent):

    selectors = {
        'self': '.routeResults'
    }

    def is_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()