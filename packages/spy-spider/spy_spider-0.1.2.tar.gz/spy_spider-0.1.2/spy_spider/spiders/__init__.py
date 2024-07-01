from spy_spider.http.request import Request


class Spider(object):
    def __init__(self):
        if not hasattr(self, "start_urls"):
            self.start_urls = []

    def start_spider(self):
        if self.start_urls:
            for start_url in self.start_urls:
                yield Request(start_url)
        else:
            if hasattr(self, "start_url") and isinstance(start_url := getattr(self, "start_url"), str):
                yield start_url
