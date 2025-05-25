from enum import Enum

from fastapi import APIRouter, Response
from fastapi.utils import deep_dict_update
from starlette.responses import FileResponse

from support.helpers import check_for_cache, get_cache_file_name
from app.routers.traps import scrape_the_table
from support.wiki_urls import wiki_urls
from support.wiki_urls import troops as troop_names

class TableType(str, Enum):
    details = "details"
    stats = "stats"


table_type_map = {"details": 0, "stats": 1}

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


@barracks_router.get("/barracks/troops")
async def get_list_all_troops():
    return {
        "troops": troop_names,
    }
    

@barracks_router.get("/barracks/troop_all_info")
async def get_troop_info(troop_name: str):
    troop_name = troop_name.lower().replace(" ", "_").replace(".", "")
    
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



@barracks_router.get("/barracks/{troop_name}/{table_type}")
async def get_troop_details(troop_name: str, table_type: TableType):
    """
    Get troop general details or statistics in CSV format.
    """
    table_index = table_type_map[table_type.value]
    cache_file = get_cache_file_name(troop_name, table_index)

    if check_for_cache(troop_name, table_index):
        return FileResponse(cache_file, media_type="text/csv")

    csv_data = await scrape_the_table(troop_name, table_index)
    return Response(csv_data, media_type="text/csv")
