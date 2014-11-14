#-*- coding:UTF-8 -*-
from spider import Spider
from spider_xml_factory import SpiderXmlFactory

# spider = Spider()
# spider.add_url("http://habrahabr.ru/")
# spider.add_domain("habrahabr.ru")
# spider.set_max_depth(3)
# spider.start()

SpiderXmlFactory().create_spider().start()