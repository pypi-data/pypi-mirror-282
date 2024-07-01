from typing import Optional, Dict, Callable


class Request(object):
    def __init__(self,
                 url: str,
                 *,
                 callback: Optional[Callable] = None,
                 method: str = "GET",
                 headers: Optional[Dict] = None,
                 body="",
                 cookies: Optional[Dict] = None,
                 meta: Optional[Dict] = None,
                 encoding="utf-8",
                 priority: int = 0,
                 proxy: Optional[Dict] = None,
                 ):
        self.url = url
        self.callback = callback
        self.method = method.upper()
        self.headers = headers if headers is not None else {}
        self.body = body
        self.cookies = cookies
        self._meta = meta if meta is not None else {}
        self.encoding = encoding
        self.priority = priority
        self.proxy = proxy

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"<{self.method} {self.url}>"

    __str__ = __repr__

    @property
    def meta(self):
        return self._meta
