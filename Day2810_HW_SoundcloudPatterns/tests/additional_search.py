#-*- coding:UTF-8 -*-
import unittest
from selenium import webdriver
from unittest_data_provider import data_provider
from Day2810_HW_SoundcloudPatterns.pages.main_page import MainPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    requests = lambda: (
        ("something",),
        ("the coolest Song",),
        ("1234567890",),
        ("aw3tpna3t-32n-ta3-j-a23t-hna-gn43",),
        (u"русская песня",)
    )

    @data_provider(requests)
    def test_addition_search_bar(self, request):
        main_page = MainPage(self._driver)
        main_page.open()
        result_page = main_page.search_bar.find(request)
        while result_page.additional_search.text() == u'':
            pass
        sub_text = result_page.additional_search.text()
        self.assertEqual(sub_text, request)


if __name__ == '__main__':
    unittest.main()
