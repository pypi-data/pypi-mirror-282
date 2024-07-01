from asyncio import create_task
from typing import Optional, Generator
from spy_spider.core.downloader import Downloader
from spy_spider.core.scheduler import Scheduler
from spy_spider.spiders import Spider
from spy_spider.http.request import Request


class Engine(object):
    def __init__(self):
        self.downloader: Optional[Downloader] = None
        self.scheduler: Optional[Scheduler] = None
        self.start_requests: Optional[Generator] = None

        self._init()

    def _init(self):
        self.downloader = Downloader()
        self.scheduler = Scheduler()

    async def start_spider(self, spider: Spider):
        self.start_requests = spider.start_spider()
        await self._run_spider()

    async def _run_spider(self):
        coro = self._crawl_spider()
        task = create_task(coro)
        await task

    async def _crawl_spider(self):
        while True:
            if (request := await self._get_request()) is not None:
                await self._crawl(request)
            else:
                try:
                    start_request = next(self.start_requests)
                except StopIteration:
                    self.start_requests = None
                except Exception as e:
                    break
                else:
                    await self._push_request(start_request)

    async def _get_request(self) -> Optional[Request]:
        return await self.scheduler.dequeue_request()

    async def _push_request(self, request: Request):
        await self._manage_push_request(request)

    async def _manage_push_request(self, request: Request):
        # todo: 去重
        await self.scheduler.enqueue_request(request)

    async def _crawl(self, request: Request):
        await self._download(request)

    async def _download(self, request: Request):
        await self.downloader.download(request)
