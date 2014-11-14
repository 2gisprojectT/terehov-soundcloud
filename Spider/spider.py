#-*- coding:UTF-8 -*-
from grab import Grab, DataNotFound
from console_logger import ConsoleLogger
from file_logger import FileLogger
from spider_link import SpiderLink


class Spider:
    def __init__(self):
        self._links = []
        self._domains = []
        self._grab = Grab()
        self._ok_codes = [200, 301, 302, 401]
        self._max_depth = 0
        self._clog = ConsoleLogger()
        self._flog = FileLogger()

    def add_url(self, url):
        self._links += [SpiderLink(url, 0)]

    def add_domain(self, domain):
        self._domains += [domain]

    def set_max_depth(self, depth):
        self._max_depth = depth

    def start(self):
        # Уже обработанные url
        visited = set([])

        while len(self._links) > 0:
            spider_link = self._links.pop(0)
            self._clog.show_progress(spider_link.url, len(visited), len(self._links) + 1)
            if spider_link.url in visited:
                continue
            visited = visited | {spider_link.url}
            # Пытаемся загрузить страницу
            is_loaded = self.try_load_url(spider_link.url)
            if not is_loaded:
                self._clog.add_error_message(self._grab.response.code, spider_link)
                self._flog.add_error_message(self._grab.response.code, spider_link)
                continue
            # Проверка на глубину
            if 0 < self._max_depth == spider_link.depth:
                continue
            # Если страница за пределами доменов, парсить не нужно
            in_domain = False
            for d in self._domains:
                if d in spider_link.url:
                    in_domain = True
                    break
            if not in_domain:
                continue
            # Парсим страницу на новые ссылки
            new_spider_links = self.get_spider_links(spider_link)
            if len(new_spider_links) == 0:
                continue
            new_spider_links = self.filter_links(new_spider_links)
            new_spider_links = self.remove_visited_links(new_spider_links, visited)
            for l in new_spider_links:
                l.parent = spider_link
            # А теперь можно и добавить в очередь
            self._links += new_spider_links

    def try_load_url(self, url):
        try:
            self._grab.go(url)
        except:
            return False
        if self._grab.response.code not in self._ok_codes:
            return False
        return True

    def get_spider_links(self, spider_link):
        objects = self._grab.doc.select("//body//a")
        spider_links = []
        for o in objects:
            try:
                url = o.attr("href")
            except DataNotFound:
                continue
            if url.startswith("/"):
                url = "http://" + self._grab.response.url_details().hostname + url
            if not url.startswith("http"):
                ind = spider_link.url.rfind("/")
                if ind == -1:
                    url = spider_link.url + "/" + url
                else:
                    url = spider_link.url[:(ind+1)] + url
            spider_links += [SpiderLink(url, spider_link.depth + 1)]
        return spider_links

    def filter_links(self, spider_links):
        filtered = []
        for l in spider_links:
            if l.url is not "" and l.url is not "#":
                filtered += [l]
        return filtered

    def remove_visited_links(self, spider_links, visited_urls):
        res = []
        for s in spider_links:
            if s.url in visited_urls:
                continue
            res += [s]
        return res