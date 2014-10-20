# -*- coding: utf-8 -*-

__author__ = 'Alexey'


from unittest import TestCase
import unittest
from selenium import webdriver


class TestSoundCloud(TestCase):
    def test_search_track_controls(self):
        d = webdriver.Firefox()
        d.get("https://soundcloud.com/")
        d.implicitly_wait(20)

        # Request input
        s = d.find_element_by_class_name("headerSearch__input")
        s.send_keys("song")
        b = d.find_element_by_class_name("headerSearch__submit")
        b.click()

        # Go to Tracks
        t = d.find_element_by_class_name("g-nav-item-sounds")
        t.click()

        # Wait for tracks
        items = d.find_elements_by_class_name("searchList__item")

        for item in items:
            # Check title
            assert item.find_element_by_class_name("soundTitle__title").is_displayed()
            assert item.find_element_by_class_name("soundTitle__username").is_displayed()

            # Check for picture
            assert item.find_element_by_class_name("sc-artwork").is_displayed()

            # Check for track buttons
            assert item.find_element_by_class_name("sc-button-like").is_displayed()
            assert item.find_element_by_class_name("sc-button-repost").is_displayed()
            assert item.find_element_by_class_name("sc-button-addtoset").is_displayed()
            assert item.find_element_by_class_name("sc-button-share").is_displayed()

            # Check waveform
            assert item.find_element_by_class_name("sound__waveform").is_displayed()

            # Upload time
            assert item.find_element_by_class_name("sound__uploadTime").is_displayed()

            # Tag
            assert item.find_element_by_class_name("soundTitle__tag").is_displayed()

            # Counters
            assert item.find_element_by_class_name("sc-ministats-plays").is_displayed()
            assert item.find_element_by_class_name("sc-ministats-likes").is_displayed()
            assert item.find_element_by_class_name("sc-ministats-reposts").is_displayed()

        # It's ok!
        d.close()

if __name__ == '__main__':
    unittest.main()