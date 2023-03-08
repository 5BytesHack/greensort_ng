from fastapi import APIRouter
from .services import get_by_id, get_by_id_and_location


api_router = APIRouter()


@api_router.get('/id/')
async def get_trashers(id: int):
    return get_by_id(id)


@api_router.get('/location/')
async def get_trashers_by_location(id: int, longitude: float, latitude: float):
    return get_by_id_and_location(id, longitude, latitude)
