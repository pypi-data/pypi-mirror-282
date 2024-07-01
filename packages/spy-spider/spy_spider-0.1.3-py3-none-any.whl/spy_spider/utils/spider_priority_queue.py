from typing import Optional
from asyncio import PriorityQueue, TimeoutError, wait_for
from spy_spider.http.request import Request


class SpiderPriorityQueue(PriorityQueue):
    def __init__(self, maxsize=0):
        super(SpiderPriorityQueue, self).__init__(maxsize=maxsize)

    async def get(self) -> Optional[Request]:
        fut = super(SpiderPriorityQueue, self).get()
        try:
            request = await wait_for(fut, timeout=0.1)
        except TimeoutError:
            request = None
        return request
