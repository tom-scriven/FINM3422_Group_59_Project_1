import requests
from lxml import html
from pathlib import Path
from urllib.parse import urljoin

PAGE_URL = "https://en.wikipedia.org/wiki/Reliance_Worldwide_Corporation"

# Fetch & parse
resp = requests.get(PAGE_URL)
doc  = html.fromstring(resp.content)

# Get the logo URL - using 0 because we know there is only one image in the infobox and the first one
src    = doc.xpath('//table[contains(@class,"infobox")]//img/@src')[0]
img_url = urljoin(PAGE_URL, src)

# Download & save
img_resp = requests.get(img_url)
Path("RWC_logo_Scraped_Final.png").write_bytes(img_resp.content)
