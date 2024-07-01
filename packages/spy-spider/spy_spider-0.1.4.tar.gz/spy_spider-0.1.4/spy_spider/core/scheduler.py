from typing import Optional
from spy_spider.utils.spider_priority_queue import SpiderPriorityQueue
from spy_spider.http.request import Request


class Scheduler(object):
    def __init__(self):
        self._request_queue: Optional[SpiderPriorityQueue] = None
        self._init()

    def _init(self):
        self._request_queue = SpiderPriorityQueue()

    async def enqueue_request(self, request: Request):
        await self._request_queue.put(request)

    async def dequeue_request(self) -> Optional[Request]:
        request = await self._request_queue.get()
        return request
