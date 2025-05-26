from fastapi import APIRouter

from .barracks import barracks_router
from .army_camp import army_camp_router
from .spell_factory import spell_factory_router
from .laboratory import laboratory_router

army_buildings_router = APIRouter(
    prefix='/army_buildings',
)

army_buildings_router.include_router(barracks_router)
army_buildings_router.include_router(army_camp_router)
army_buildings_router.include_router(spell_factory_router)
army_buildings_router.include_router(laboratory_router)
