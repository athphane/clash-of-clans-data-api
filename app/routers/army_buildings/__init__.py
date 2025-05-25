from fastapi import APIRouter

from .barracks import barracks_router

army_buildings_router = APIRouter(
    prefix='/army_buildings',
)

army_buildings_router.include_router(barracks_router)
