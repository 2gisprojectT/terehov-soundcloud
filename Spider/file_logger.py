import datetime
import time


class FileLogger:
    def __init__(self):
        self._filename = "log.txt"
        open(self._filename, "w").close()

    def add_error_message(self, code, spider_link):
        file = open(self._filename, "a")
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        file.write("===== " + st + " Error code " + str(code) + " =====\n")
        if spider_link.parent is not None:
            file.write("page url: " + spider_link.parent.url + "\n")
        file.write("link url: " + spider_link.url + "\n")
        file.write("page depth: " + str(spider_link.depth) + "\n\n")
        file.close()