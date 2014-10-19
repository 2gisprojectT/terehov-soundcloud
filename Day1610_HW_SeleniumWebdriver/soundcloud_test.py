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
            assert item.find_element_by_class_name("soundTitle__title")
            assert item.find_element_by_class_name("soundTitle__username")

            # Check for picture
            assert item.find_element_by_class_name("sc-artwork")

            # Check for track buttons
            assert item.find_element_by_class_name("sc-button-like")
            assert item.find_element_by_class_name("sc-button-repost")
            assert item.find_element_by_class_name("sc-button-addtoset")
            assert item.find_element_by_class_name("sc-button-share")

            # Check waveform
            assert item.find_element_by_class_name("sound__waveform")

            # Upload time
            assert item.find_element_by_class_name("sound__uploadTime")

            # Tag
            assert item.find_element_by_class_name("soundTitle__tag")

            # Counters
            assert item.find_element_by_class_name("sc-ministats-plays")
            assert item.find_element_by_class_name("sc-ministats-likes")
            assert item.find_element_by_class_name("sc-ministats-reposts")

        # It's ok!
        d.close()

    # def test_search_track_controls(self):
    #     d = webdriver.Firefox()
    #     d.get("https://soundcloud.com/")
    #     # Request input
    #     s = WebDriverWait(d, 10).until(
    #         expected_conditions.presence_of_element_located((By.CLASS_NAME, "headerSearch__input"))
    #     )
    #     s.send_keys("song")
    #     b = d.find_element_by_class_name("headerSearch__submit")
    #     b.click()
    #     # Go to Tracks
    #     t = WebDriverWait(d, 10).until(
    #         expected_conditions.presence_of_element_located((By.CLASS_NAME, "g-nav-item-sounds"))
    #     )
    #     t.click()
    #     # Wait for tracks
    #     try:
    #         WebDriverWait(d, 10).until(
    #             expected_conditions.presence_of_element_located((By.CLASS_NAME, "searchList__item"))
    #         )
    #     except:
    #         self.fail("No items at response!")
    #     # Check title
    #     try:
    #         song = d.find_element_by_class_name("soundTitle__title")
    #         author = d.find_element_by_class_name("soundTitle__username")
    #     except:
    #         self.fail("There are no title!")
    #     # Check for picture
    #     try:
    #         pict = d.find_element_by_class_name("sc-artwork")
    #     except:
    #         self.fail("There is no picture!")
    #     # Check for track buttons
    #     try:
    #         like = d.find_element_by_class_name("sc-button-like")
    #         repost = d.find_element_by_class_name("sc-button-repost")
    #         add = d.find_element_by_class_name("sc-button-addtoset")
    #         share = d.find_element_by_class_name("sc-button-share")
    #     except:
    #         self.fail("Track response contains not all of buttons")
    #     # Check waveform
    #     try:
    #         wave = d.find_element_by_class_name("sound__waveform")
    #     except:
    #         self.fail("There is no waveform!")
    #     # Upload time
    #     try:
    #         upload = d.find_element_by_class_name("sound__uploadTime")
    #     except:
    #         self.fail("There is no upload time!")
    #     # Tag
    #     try:
    #         tag = d.find_element_by_class_name("soundTitle__tag")
    #     except:
    #         self.fail("There is no tag!")
    #     # Counters
    #     try:
    #         plays = d.find_element_by_class_name("sc-ministats-plays")
    #         likes = d.find_element_by_class_name("sc-ministats-likes")
    #         reposts = d.find_element_by_class_name("sc-ministats-reposts")
    #         comments = d.find_element_by_class_name("sc-ministats-comments")
    #     except:
    #         self.fail("There is no counters!")
    #     # It's ok!
    #     # d.close()

if __name__ == '__main__':
    unittest.main()