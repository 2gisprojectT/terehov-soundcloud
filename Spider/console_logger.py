import os


class ConsoleLogger:
    def __init__(self):
        self._last_errors = []
        self._max_errors = 5
        self._max_len = 80

    def add_error_message(self, code, spider_link):
        self._last_errors += [
            "Error code " + str(code)
            + ", depth " + str(spider_link.depth)
            + ", url: " + spider_link.url]
        while len(self._last_errors) > self._max_errors:
            self._last_errors.pop(0)

    def show_progress(self, current, handled, total):
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(current) > self._max_len:
            current = current[:(self._max_len / 2)] + " ... " + current[-(self._max_len / 2):]
        print("===Spider handles: " + str(current))
        print("Already handled: " + str(handled))
        print("In queue: " + str(total))
        if len(self._last_errors) == 0:
            print("===No errors")
        else:
            print("===Last errors:")
            for l in self._last_errors:
                print(l)
