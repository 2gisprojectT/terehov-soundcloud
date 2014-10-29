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

    def test_follow_buttons(self):
        main_page = MainPage(self._driver)
        main_page.open()
        result_page = main_page.search_bar.find("somebody")
        result_page.categories.open("people")
        sleep(1)
        people = result_page.found_people
        for human in people:
            self.assertTrue(human.is_follow_button_displayed())


if __name__ == '__main__':
    unittest.main()
