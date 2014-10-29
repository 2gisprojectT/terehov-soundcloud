import unittest
from selenium import webdriver
from Day2810_HW_SoundcloudPatterns.pages.main_page import MainPage
from time import sleep


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    def test_player_title(self):
        main_page = MainPage(self._driver)
        main_page.open()
        result_page = main_page.search_bar.find("something")
        track = result_page.found_tracks[0]
        track_title = track.title()
        track.play()
        sleep(1)
        player_title = result_page.player.title()
        self.assertEqual(track_title, player_title)

if __name__ == '__main__':
    unittest.main()
