from aiohttp import web
from greensort.urls import urls
from aiohttp_cors import setup, ResourceOptions


app = web.Application()
app.add_routes(urls)
cors = setup(app, defaults={
    '*': ResourceOptions(
        allow_credentials=True,
        expose_headers='*',
        allow_headers='*',
        allow_methods='*'
    )
})
web.run_app(app)
