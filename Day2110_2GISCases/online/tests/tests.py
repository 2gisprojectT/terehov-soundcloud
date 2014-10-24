#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from Day2110_2GISCases.online.helpers.page import Page


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")

    def tearDown(self):
        self.driver.close()

    def test_share(self):
        page = self.page
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

    def test_transport(self):
        page = self.page
        page.search_bar.change_mode(page.search_bar.selectors['mode_transport'])
        page.search_bar.search_transport(u"Площадь Маркса", u"Заельцовская")
        self.assertTrue(page.route_result.is_displayed(), "There are no route results!")

if __name__ == '__main__':
    unittest.main()