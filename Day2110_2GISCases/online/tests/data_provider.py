#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from unittest_data_provider import data_provider
from Day2110_2GISCases.online.helpers.page import Page


class SeleniumTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    requests = lambda: (
        (u"123423525wefasfasdf", False),
        (u"j-jwg-9hwa-gh3-hg-ahwg", False),
        (u"2ygi   2g2 23g2g2  3g", False),
        (u"Магазин", True),
        (u"Кино-сити", True),
        (u"Горский", True)
    )

    @data_provider(requests)
    def test_search(self, request, result):
        page = Page(self._driver)
        page.open("http://2gis.ru")
        page.search_bar.search(request)
        self.assertEqual(page.search_result.is_empty, not result, "Wrong result!")

if __name__ == '__main__':
    unittest.main()