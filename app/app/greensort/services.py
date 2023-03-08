from math import atan, cos, sin
from motor.motor_asyncio import AsyncIOMotorClient


def distance_between_coords(coord0, coord1):
    lat0, lon0 = coord0
    lat1, lon1 = coord1
    delta = lat1 - lat0
    return abs(atan((((cos(lon1) * sin(delta)) ** 2 + (cos(lon0) * sin(lat1) -
               sin(lon0) * cos(lon1) * cos(delta)) ** 2) ** 0.5) /
               sin(lon0) * sin(lon1) + cos(lon0) * cos(lon1) * cos(delta)))


async def get_by_id(id):
    client = AsyncIOMotorClient('mongo', 27017)
    db = client.db
    collection = db.trashers
    trashers = []
    async for obj in collection.find({'types': id}):
        trashers.append({
            'address': obj['address'],
            'coords': obj['coords']
        })
    return {'trashers': trashers}


async def get_by_id_and_location(id, longitude, latitude):
    coords = (latitude, longitude)
    client = AsyncIOMotorClient('mongo', 27017)
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
        distance = distance_between_coords(obj['coords'], coords)
        if distance < m:
            neariest = obj['coords']
            m = distance
    return {
        'neariest': neariest,
        'trashers': trashers
    }
