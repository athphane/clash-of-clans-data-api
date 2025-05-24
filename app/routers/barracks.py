from enum import Enum

from fastapi import APIRouter, Response
from starlette.responses import FileResponse

from support.helpers import check_for_cache, get_cache_file_name
from app.routers.traps import scrape_the_table

barracks_router = APIRouter(
    # prefix=
)


@barracks_router.get("/barracks")
async def bomb_stats_csv():
    THING = 'barracks'
    if check_for_cache(THING, 0):
        with open(get_cache_file_name(THING, 0), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, 0)

    return Response(csv_data, media_type='text/csv')


class TableType(str, Enum):
    details = "details"
    stats = "stats"


table_type_map = {"details": 0, "stats": 1}


@barracks_router.get("/barracks/{thing}/{table_type}")
async def get_troop_details(thing: str, table_type: TableType):
    """
    Get troop general details or statistics in CSV format.
    """
    table_index = table_type_map[table_type.value]
    cache_file = get_cache_file_name(thing, table_index)

    if check_for_cache(thing, table_index):
        return FileResponse(cache_file, media_type="text/csv")

    csv_data = await scrape_the_table(thing, table_index)
    return Response(csv_data, media_type="text/csv")
