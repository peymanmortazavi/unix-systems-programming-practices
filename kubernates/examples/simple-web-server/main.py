from aiohttp import web

async def hello(request):
    return web.Response(text="Hello Peyman!")


app = web.Application()
app.add_routes([
    web.get('/', hello),
])

web.run_app(app, port=3000)
