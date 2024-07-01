import httpx


class Downloader(object):
    def __init__(self):
        pass

    async def download(self, request):
        await self._download(request)

    async def _download(self, request):
        response = httpx.get(request.url)
        print(response)
