import csv
import io
import os

import httpx
from fastapi import APIRouter, HTTPException, Response
from lxml import html

from app.wiki_urls import wiki_urls

router = APIRouter(
    prefix='/traps'
)

def get_cache_file_name(file_name: str, table: int) -> str:
    return f"cache/{file_name}-{table}.csv"

def check_for_cache(file_name, table: int) -> bool:
    return os.path.exists(get_cache_file_name(file_name, table))

async def scrape_bomb(path: str, table: int) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.get(wiki_urls['bomb'])
    if r.status_code != 200:
        raise HTTPException(502, "Failed to fetch source page")

    doc = html.fromstring(r.text)
    tables = doc.xpath('//table[contains(@class,"wikitable")]')
    if len(tables) < 2:
        raise HTTPException(500, "Bomb stats table not found")
    table = tables[table]

    output = io.StringIO()
    writer = csv.writer(output)
    for tr in table.xpath(".//tr"):
        writer.writerow([cell.text_content().strip() for cell in tr.xpath("./th|./td")])

    csv_data = output.getvalue()
    with open(get_cache_file_name(path, table), "w", encoding="utf-8", newline="") as f:
        f.write(csv_data)
    return csv_data

@router.get("/bomb-details")
async def bomb_details_csv():
    BOMB = 'bomb'
    if check_for_cache(BOMB, 1):
        with open(get_cache_file_name(BOMB, 1), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_bomb(BOMB, 1)

    return Response(csv_data, media_type='text/csv')


@router.get("/bomb")
async def bomb_stats_csv():
    BOMB = 'bomb'
    if check_for_cache(BOMB, 0):
        with open(get_cache_file_name(BOMB, 0), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_bomb(BOMB, 0)

    return Response(csv_data, media_type='text/csv')


async def scrape_spring_trap(path: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.get(wiki_urls['spring_trap'])
    if r.status_code != 200:
        raise HTTPException(502, "Failed to fetch source page")

    doc = html.fromstring(r.text)
    tables = doc.xpath('//table[contains(@class,"wikitable")]')
    if len(tables) < 2:
        raise HTTPException(500, "Bomb stats table not found")
    table = tables[1]

    output = io.StringIO()
    writer = csv.writer(output)
    for tr in table.xpath(".//tr"):
        writer.writerow([cell.text_content().strip() for cell in tr.xpath("./th|./td")])

    csv_data = output.getvalue()
    with open(get_cache_file_name(path), "w", encoding="utf-8", newline="") as f:
        f.write(csv_data)
    return csv_data

@router.get("/spring_trap")
async def bomb_stats_csv():
    BOMB = 'spring_trap'
    if check_for_cache(BOMB):
        with open(get_cache_file_name(BOMB), "r", encoding="utf-8") as f:
            csv_data = f.read()
    else:
        csv_data = await scrape_spring_trap(BOMB)

    return Response(csv_data, media_type='text/csv')