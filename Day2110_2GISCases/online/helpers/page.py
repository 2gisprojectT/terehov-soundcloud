class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._route_result = None
        self._share_bar = None

    @property
    def search_bar(self):
        from Day2110_2GISCases.online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from Day2110_2GISCases.online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def route_result(self):
        from Day2110_2GISCases.online.helpers.route_results import RouteResult

        if self._route_result is None:
            self._route_result = RouteResult(self.driver, self.driver.find_element_by_css_selector(RouteResult.selectors['self']))
        return self._route_result

    @property
    def share_bar(self):
        from Day2110_2GISCases.online.helpers.share_bar import ShareBar

        if self._share_bar is None:
            self._share_bar = ShareBar(self.driver)
        return self._share_bar

    def open(self, url):
        self.driver.get(url)

