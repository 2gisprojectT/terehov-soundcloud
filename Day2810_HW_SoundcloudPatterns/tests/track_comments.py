from time import sleep
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
        pass

    def test_comments(self):
        main_page = MainPage(self._driver)
        main_page.open()
        result_page = main_page.search_bar.find("something")
        tracks = result_page.found_tracks
        t = tracks[0]
        t.show_comment_input()
        self.assertTrue(t.is_comment_input_displayed(), "no comment bar!")


if __name__ == '__main__':
    unittest.main()
