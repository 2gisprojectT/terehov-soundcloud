#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from Day2110_2GISCases.online.helpers.page import Page


class SeleniumTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    def test_share(self):
        page = Page(self._driver)
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
        self.assertGreaterEqual(after_count, 0, "Wrong count!")

    def test_transport(self):
        page = Page(self._driver)
        page.open("http://2gis.ru")
        page.search_bar.change_mode(page.search_bar.selectors['mode_transport'])
        page.search_bar.search_transport(u"Площадь Маркса", u"Заельцовская")
        self.assertTrue(page.route_result.is_displayed(), "There are no route results!")

if __name__ == '__main__':
    unittest.main()