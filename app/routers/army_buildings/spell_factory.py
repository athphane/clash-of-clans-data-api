from fastapi import APIRouter, Response

from app.enums import Spells, TableType
from app.routers.traps import scrape_the_table
from support.helpers import check_for_cache, get_cache_file_name
from support.wiki_urls import spells, wiki_urls

spell_factory_router = APIRouter(
    prefix="/spell_factory",
)


@spell_factory_router.get("/", operation_id='SpellFactoryStats')
async def spell_factory():
    """
    Get information about the Spell Factory, what it unlocks and its stats.    
    """

    THING = 'spell_factory'
    if check_for_cache(THING, TableType.stats.value):
        with open(get_cache_file_name(THING, TableType.stats.value), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, TableType.stats.value)

    return Response(csv_data, media_type='text/csv')


@spell_factory_router.get("/dark_spell_factory", operation_id='DarkSpellFactoryStats')
async def dark_spell_factory():
    """
    Get information about the Dark Spell Factory, what it unlocks and its stats.    
    """

    THING = 'dark_spell_factory'
    if check_for_cache(THING, TableType.stats.value):
        with open(get_cache_file_name(THING, TableType.stats.value), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_the_table(THING, TableType.stats.value)

    return Response(csv_data, media_type='text/csv')


@spell_factory_router.get("/spells", operation_id='GetAllSpells')
async def get_list_all_spells():
    """
    Get a list of all spells available
    """
    return {
        "spells": spells,
    }

    
@spell_factory_router.get("/spell_all_info", operation_id='GetAllSpellInfo')
async def get_spell_info(spell_name: Spells):
    """
    Get all the available information for a specific spell.
    """
    spell_info = ""

    spell_data = wiki_urls.get(spell_name)

    print(f"Fetching info for spell: {spell_name}")

    for troop_table in spell_data['tables'].keys():
        troop_cache_file_name = get_cache_file_name(spell_name, troop_table)

        if check_for_cache(troop_cache_file_name, troop_table):
            spell_info += f"{spell_name} : {troop_table}:\n"
            spell_info += open(troop_cache_file_name, "r", encoding="utf-8").read() + "\n"
            spell_info += "\n"
        else:
            spell_info += f"{spell_name} : {troop_table}:\n"
            spell_info += await scrape_the_table(spell_name, troop_table) + "\n"
            spell_info += "\n"

    return Response(spell_info.strip(), media_type="text/csv")