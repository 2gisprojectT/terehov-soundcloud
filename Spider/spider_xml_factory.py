from xml.dom.minidom import *
from spider import Spider


class SpiderXmlFactory:
    def __init__(self):
        self._filename = "params.xml"
        self._parameters = "parameters"
        self._page = "page"
        self._domain = "domain"
        self._depth = "depth"

    def create_spider(self):
        spider = Spider()

        xml = parse(self._filename)
        params = xml.getElementsByTagName(self._parameters)
        if params is not None:
            params = params[0]

            pages = params.getElementsByTagName(self._page)
            for page in pages:
                print(page.firstChild.data)
                spider.add_url(page.firstChild.data)

            domains = params.getElementsByTagName(self._domain)
            for domain in domains:
                print(domain.firstChild.data)
                spider.add_domain(domain.firstChild.data)

            depth = params.getElementsByTagName(self._depth)
            if depth is not None:
                depth = depth[0]
                print(depth.firstChild.data)
                spider.set_max_depth(depth.firstChild.data)

        return spider