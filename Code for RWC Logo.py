import requests
from lxml import html
from pathlib import Path
from urllib.parse import urljoin

PAGE_URL = "https://en.wikipedia.org/wiki/Reliance_Worldwide_Corporation"

# User-Agent to avoid 403 eroor from wikipedia 
# #allows us to actually view the png in vs code - couldn't until I added this
HEADERS = {"User-Agent": "finm@assignment.com"}

# Fetch & parse
resp = requests.get(PAGE_URL, headers=HEADERS)
doc = html.fromstring(resp.content)

# Locate the first infobox image
src = doc.xpath('//table[contains(@class,"infobox")]//img/@src')[0]
img_url = urljoin(PAGE_URL, src)

# Download & save
img_resp = requests.get(img_url, headers=HEADERS)
ext = Path(src).suffix  
Path(f"RWC{ext}").write_bytes(img_resp.content)
