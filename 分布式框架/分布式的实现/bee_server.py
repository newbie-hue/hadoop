from sanic import Sanic
from sanic import  response
from urlpool import  UrlPool

#��ʼ��urlpool,�ܾ���Ҫ�����޸�
urlpool = UrlPool(__file__)

#��ʼ��url
urlpool.add('https://news.sina.com.cn/')
app = Sanic(__name__)

@app.listener("after_server_stop")
async def cache_urlpool(app,loop):
    global urlpool
    print("caching urlpool after_server_stop")
    del urlpool
    print("bye!")

@app.route("/task")
async def task_get(request):
    count = request.args.get("count",10)
    try:
        count = int(count)
    except:
        count = 10
    urls = urlpool.pop(count)
    return response.json(urls)

@app.route("/task",methods=["POST",])
async def task_post(requrst):
    result = requrst.json()
    urlpool.set_status(result['url'],result['status'])
    if result['url_real'] != result['url']:
        urlpool.set_status(result["url_real"],result["status"])
    if result["newurls"]:
        print("receive URLs:",len(result["newurls"]))
        for url in result["newurls"]:
            urlpool.add(url)
    return response.text("ok")

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port = 8080,
        debug=False,
        access_log=False,
        workers=1
    )