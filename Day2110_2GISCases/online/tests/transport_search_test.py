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

        page.search_bar.change_mode(page.search_bar.selectors['mode_transport'])
        page.search_bar.search_transport(u"Площадь Маркса", u"Заельцовская")

        self.assertTrue(page.route_result.is_displayed(), "There are no route results!")
        driver.close()

if __name__ == '__main__':
    unittest.main()