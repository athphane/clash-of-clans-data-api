import asyncio

from support.scraper import scrape_the_table
from support.wiki_urls import wiki_urls

if __name__ == '__main__':
    async def main():
        for key in wiki_urls:
            values = wiki_urls[key]
            for tables in values['tables']:
                print(f"Scraping {key} - {tables}")
                table_data = await scrape_the_table(key, tables)
                print(table_data)


    asyncio.run(main())
