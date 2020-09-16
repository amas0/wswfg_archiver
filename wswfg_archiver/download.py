import asyncio
from datetime import date
from typing import List, Optional

import aiohttp
import bs4

BASE_URL = 'http://willsaveworldforgold.com/comics/'


class Image:
    def __init__(self, dat: date, url: str, content: Optional[bytes]):
        self.dat = dat
        self.url = url
        self.content = content


def get_image_list(html: str) -> List[Image]:
    def parse_date(link: str) -> date:
        date_str = link[:10]
        y, m, d = date_str.split('-')
        return date(year=int(y), month=int(m), day=int(d))

    soup = bs4.BeautifulSoup(html, 'html.parser')
    links = [link.attrs.get('href') for link in soup.find_all('a')]
    links = [link for link in links if link.endswith('png')]
    dates = [parse_date(link) for link in links]
    urls = [f'{BASE_URL}{link}' for link in links]
    return [Image(dat=dat, url=url, content=None) for dat, url in zip(dates, urls)]


async def get_all_available_image_links(session: aiohttp.ClientSession) -> List[Image]:
    async with session.get(BASE_URL) as resp:
        text = await resp.text()
        return get_image_list(text)


async def download_image(img: Image, session: aiohttp.ClientSession) -> Image:
    async with session.get(img.url) as resp:
        content = await resp.read()
        return Image(dat=img.dat, url=img.url, content=content)


async def download_images_async(start_date: date = date(2011, 9, 12), end_date: Optional[date] = date.today()) -> List[Image]:
    connector = aiohttp.TCPConnector(limit=8)
    async with aiohttp.ClientSession(connector=connector) as session:
        image_links = await get_all_available_image_links(session)
        to_download = [img for img in image_links if start_date <= img.dat <= end_date]
        print(f'Downloading {len(to_download)} images...', end='')
        downloaded_images = await asyncio.gather(*[download_image(img, session) for img in to_download])
        print('done.')
        return downloaded_images


def download_images(start_date: date = date(2011, 9, 12), end_date: date = date.today()) -> List[Image]:
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(download_images_async(start_date=start_date, end_date=end_date))
    loop.close()
    return result
