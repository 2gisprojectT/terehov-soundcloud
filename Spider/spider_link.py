class SpiderLink:
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth
        self.parent = None