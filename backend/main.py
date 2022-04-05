from aiohttp import web
from greensort.urls import urls
from xls_to_mongo import main

app = web.Application()
app.add_routes(urls)
main()
web.run_app(app)
