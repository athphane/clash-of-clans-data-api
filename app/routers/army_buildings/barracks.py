from fastapi import APIRouter, Response
from starlette.responses import FileResponse

from app.enums import TableType, Troops
from app.routers.traps import scrape_the_table
from support.helpers import check_for_cache, get_cache_file_name
from support.wiki_urls import wiki_urls

table_type_map = {"details": 0, "stats": 1}

barracks_router = APIRouter(
    prefix="/barracks",
)


@barracks_router.get("/")
async def barracks():
    THING = 'barracks'
    if check_for_cache(THING, 'stats'):
        with open(get_cache_file_name(THING, 'stats'), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, 'stats')

    return Response(csv_data, media_type='text/csv')


@barracks_router.get("/troops")
async def get_list_all_troops():
    return {
        "troops": list(Troops),
    }


@barracks_router.get("/troop_all_info")
async def get_troop_info(troop_name: Troops):
    troop_info = ""

    troop_data = wiki_urls.get(troop_name)

    print(f"Fetching info for troop: {troop_name}")

    for troop_table in troop_data['tables'].keys():
        troop_cache_file_name = get_cache_file_name(troop_name, troop_table)

        if check_for_cache(troop_cache_file_name, troop_table):
            troop_info += f"{troop_name} : {troop_table}:\n"
            troop_info += open(troop_cache_file_name, "r", encoding="utf-8").read() + "\n"
            troop_info += "\n"
        else:
            troop_info += f"{troop_name} : {troop_table}:\n"
            troop_info += await scrape_the_table(troop_name, troop_table) + "\n"
            troop_info += "\n"

    return Response(troop_info.strip(), media_type="text/csv")


@barracks_router.get("/{troop_name}/{table_type}")
async def get_troop_details(troop_name: Troops, table_type: TableType):
    """
    Get troop general details or statistics in CSV format.
    """
    cache_file = get_cache_file_name(troop_name, table_type.value)

    if check_for_cache(troop_name, table_type.value):
        return FileResponse(cache_file, media_type="text/csv")

    csv_data = await scrape_the_table(troop_name, table_type.value)
    return Response(csv_data, media_type="text/csv")
