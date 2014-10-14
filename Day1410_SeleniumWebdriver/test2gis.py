# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Alexey'


from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test2Gis(TestCase):

    def test_search_has_items(self):
        driver = webdriver.Firefox()
        driver.get("http://www.2gis.ru")
        search_input = driver.find_element_by_class_name("suggest__input")
        search_input.send_keys(u"Город")
        search_btn = driver.find_element_by_class_name("searchBar__submit")
        search_btn.click()
        places_btn = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "mixedResults__geoTab"))
        )
        places_btn.click()
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "miniCard"))
            )
        except:
            self.fail("Has no elements")
        driver.close()

if __name__ == '__main__':
    unittest.main()