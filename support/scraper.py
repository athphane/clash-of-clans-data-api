import csv
import io

import httpx
from fastapi import HTTPException
from lxml import html

from app.enums import TableType
from support.helpers import get_cache_file_name
from support.wiki_urls import wiki_urls


async def scrape_the_table(wiki_key: str, return_table: TableType) -> str:
    """
    Scrapes a specific table from a Wikipedia page, converts it to CSV, and caches the result.

    Args:
        wiki_key (str): Key to select the Wikipedia URL and table index from wiki_urls.
        return_table (str, optional): Table identifier to select the correct table. Defaults to 'stats'.

    Returns:
        str: The scraped table in CSV format.

    Raises:
        HTTPException: If the page cannot be fetched or the required table is not found.
    """
    wiki_url = wiki_urls[wiki_key]['url']
    return_table_idx = wiki_urls[wiki_key]['tables'].get(return_table)

    # Fetch the Wikipedia page asynchronously
    async with httpx.AsyncClient() as client:
        r = await client.get(wiki_url)

    if r.status_code != 200:
        raise HTTPException(502, "Failed to fetch source page!")

    # Parse the HTML content
    doc = html.fromstring(r.text)
    tables = doc.xpath('//table[contains(@class,"wikitable")]')

    # Ensure the required table exists
    if len(tables) < 2:
        raise HTTPException(500, "Stats table was not found!")

    table = tables[return_table_idx]

    # Convert the table to CSV format
    output = io.StringIO()
    writer = csv.writer(output)

    for tr in table.xpath(".//tr"):
        writer.writerow([cell.text_content().strip() for cell in tr.xpath("./th|./td")])

    csv_data = output.getvalue()

    # Save the CSV data to a cache file
    with open(get_cache_file_name(wiki_key, return_table), "w", encoding="utf-8", newline="") as f:
        f.write(csv_data)

    return csv_data
