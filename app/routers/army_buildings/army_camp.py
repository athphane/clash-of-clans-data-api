from fastapi import APIRouter, Response

from app.enums import TableType
from app.routers.traps import scrape_the_table
from support.helpers import check_for_cache, get_cache_file_name

army_camp_router = APIRouter(
    prefix="/army_camp",
)


@army_camp_router.get("/", operation_id='ArmyCampStats')
async def army_camp():
    THING = 'army_camp'
    if check_for_cache(THING, TableType.stats.value):
        with open(get_cache_file_name(THING, TableType.stats.value), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, TableType.stats.value)

    return Response(csv_data, media_type='text/csv')
