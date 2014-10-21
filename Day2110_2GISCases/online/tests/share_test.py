#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from Day2110_2GISCases.online.helpers.page import Page

class SeleniumTest(TestCase):

    def test_share(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'синема')
        before_count = page.search_result.count
        before_text = page.search_bar.text

        page.share_bar.open()
        link = page.share_bar.share_link
        page.open(link)

        after_count = page.search_result.count
        after_text = page.search_bar.text
        self.assertEqual(before_count, after_count, "Wrong share link!")
        self.assertEqual(before_text, after_text, "Wrong share link!")
        driver.close()

if __name__ == '__main__':
    unittest.main()