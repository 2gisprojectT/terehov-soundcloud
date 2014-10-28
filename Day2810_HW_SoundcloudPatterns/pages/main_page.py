from Day2810_HW_SoundcloudPatterns.components.search_bar import SearchBar


class MainPage:
    _selectors = {
        "search_bar": "header__search"
    }

    def __init__(self, driver):
        """
        :param driver: WebDriver
        """
        self.driver = driver
        self.url = "https://soundcloud.com/"

    def open(self):
        self.driver.get(self.url)

    @property
    def search_bar(self):
        el = self.driver.find_element_by_class_name(self._selectors["search_bar"])
        return SearchBar(self.driver, el)