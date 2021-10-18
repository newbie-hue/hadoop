import aiohttp
import json
import asyncio
import traceback
import time

class CrawlerClient:
    def __init__(self):
        self._workers = 0
        self.workers_max = 10
        self.server_host = "localhost"
        self.server_port = 8080
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.queue = asyncio.Queue

    async def get_url(self):
        count = self.workers_max-self.queue.qsize()
        if count <= 0:
            print("no need to get urls this time")

        url = "http://%S:%S/task?count=%s" % (self.server_host,self.server_port,count)
        try:
            async with self.session.get(url,timeout = 3) as response:
                if response.status not in [200,201]:
                    return
                jsn = await response.text()
                urls = json.loads(jsn)
                msg = ('get_urls() to get [%s] but got[%s],@%s') % (count,len(urls),time.strftime('%Y-%m-%d %H:%M:%S'))
                print(msg)
                for lv in urls.items():
                    await self.queue.put(lv)
                print()
        except:
            traceback.print_exc()
            return

    async def send_result(self,result):
        '''
        result = {
        "url¡°:url,
        'url_real':response.url,
        'status':status,
        "newurls":newurls,
        }
        '''
        url = "http://%S:%S/task" % (self.server_host,self.server_port)
        try:
            async with self.session.post(url,json = result,timeout = 3) as response:
                response.status
        except:
            traceback.print_exc()
            pass

