from math import atan, cos, sin

from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient


def distance_between_coords(coord0, coord1):
    lat0, lon0 = [float(x) for x in coord0.split(',')]
    lat1, lon1 = [float(x) for x in coord1.split(',')]
    delta = lat1 - lat0
    return abs(atan((((cos(lon1) * sin(delta)) ** 2 + (cos(lon0) * sin(lat1) -
               sin(lon0) * cos(lon1) * cos(delta)) ** 2) ** 0.5) /
               sin(lon0) * sin(lon1) + cos(lon0) * cos(lon1) * cos(delta)))


async def get_by_id(request: web.Request):
    """Получает в форме POST запросом id типа мусора и возвращает json из всех подходящих мусорок"""
    if request.method == 'POST':
        form = await request.post()
    else:
        form = request.query
    id = int(form['id'])
    client = AsyncIOMotorClient('host.docker.internal', 27017)
    db = client.db
    collection = db.trashers
    trashers = []
    async for obj in collection.find({'types': id}):
        trashers.append({
            'address': obj['address'],
            'coords': obj['coords']
        })
    return web.json_response({'trashers': trashers})


async def get_by_id_and_location(request):
    if request.method == 'POST':
        form = await request.post()
    else:
        form = request.query
    id = int(form.get('id'))
    latitude = form.get('latitude')
    longitude = form.get('longitude')
    coords = latitude + ',' + longitude
    client = AsyncIOMotorClient('host.docker.internal', 27017)
    db = client.db
    collection = db.trashers
    m = 100000.0
    trashers = []
    neariest = None
    async for obj in collection.find({'types': id}):
        trashers.append({
            'address': obj['address'],
            'coords': obj['coords']
        })
        if distance_between_coords(obj['coords'], coords) < m:
            neariest = obj['coords']
            m = distance_between_coords(obj['coords'], coords)
    return web.json_response({
        'neariest': neariest,
        'trashers': trashers
    })
