from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import datetime
concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print(status, url)

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    start = datetime.datetime.now()
    for i in range(10000):
        q.put('http://localhost:4566/async')
    q.join()
    end = datetime.datetime.now() - start
    print(end)
except KeyboardInterrupt:
    sys.exit(1)