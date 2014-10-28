import unittest
from selenium import webdriver
from Day2810_HW_SoundcloudPatterns.pages.main_page import MainPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    def test_categories(self):
        main_page = MainPage(self._driver)
        main_page.open()
        result_page = main_page.search_bar.find("something")
        cats = result_page.categories
        msg = "not all categories"
        self.assertTrue(cats.is_everything_displayed(), msg)
        self.assertTrue(cats.is_tracks_displayed(), msg)
        self.assertTrue(cats.is_playlists_displayed(), msg)
        self.assertTrue(cats.is_people_displayed(), msg)
        self.assertTrue(cats.is_groups_displayed(), msg)

if __name__ == '__main__':
    unittest.main()
