from fastapi import APIRouter, Response

from app.enums import TableType
from app.routers.traps import scrape_the_table
from support.helpers import check_for_cache, get_cache_file_name

hero_hall_router = APIRouter(
    prefix="/hero-hall",
)


@hero_hall_router.get("/", operation_id='HeroHallStats')
async def hero_hall():
    THING = 'hero_hall'
    if check_for_cache(THING, TableType.stats.value):
        with open(get_cache_file_name(THING, TableType.stats.value), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, TableType.stats.value)

    return Response(csv_data, media_type='text/csv')
