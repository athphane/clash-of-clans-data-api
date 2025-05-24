from fastapi import APIRouter, Response

from support.helpers import get_cache_file_name, check_for_cache
from support.scraper import scrape_the_table

traps_router = APIRouter(
    prefix='/traps'
)


@traps_router.get("/bomb/stats")
async def bomb_stats_csv():
    THING = 'bomb'
    RETURN_TABLE = 'stats'
    if check_for_cache(THING, RETURN_TABLE):
        with open(get_cache_file_name(THING, RETURN_TABLE), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, RETURN_TABLE)

    return Response(csv_data, media_type='text/csv')


@traps_router.get("/bomb/details")
async def bomb_details_csv():
    THING = 'bomb'
    RETURN_TABLE = 'details'

    if check_for_cache(THING, RETURN_TABLE):
        with open(get_cache_file_name(THING, RETURN_TABLE), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, RETURN_TABLE)

    return Response(csv_data, media_type='text/csv')


@traps_router.get("/spring_trap/stats")
async def bomb_stats_csv():
    THING = 'spring_trap'
    RETURN_TABLE = 'stats'

    if check_for_cache(THING, RETURN_TABLE):
        with open(get_cache_file_name(THING, RETURN_TABLE), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, RETURN_TABLE)

    return Response(csv_data, media_type='text/csv')
