# examples/2_async/async.py
import asyncio

from celery_add import run_et
from japronto import Application


# This is a synchronous handler.
def synchronous(request):
    return request.Response(json={'hello-everyone': run_et.delay().get()})


# This is an asynchronous handler, it spends most of the time in the event loop.
# It wakes up every second 1 to print and finally returns after 3 seconds.
# This does let other handlers to be executed in the same processes while
# from the point of view of the client it took 3 seconds to complete.
async def asynchronous(request):
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, run_et.delay().get())
    return request.Response(text='Done')


app = Application()

r = app.router
r.add_route('/sync', synchronous)
r.add_route('/async', asynchronous)

# Finally start our server and handle requests until termination is
# requested. Enabling debug lets you see request logs and stack traces.
app.run(debug=True)
