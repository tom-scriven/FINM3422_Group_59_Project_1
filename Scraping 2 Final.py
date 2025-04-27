import requests
from lxml import html
from pathlib import Path
from urllib.parse import urljoin

PAGE_URL = "https://www.rwc.com/investors/business-overview"

# Fetch & parse
resp = requests.get(PAGE_URL)
doc = html.fromstring(resp.content)

# Finding the two charts using the path “ratio_unlocked_medium/public/media-image” to ensure they are correct
srcs = doc.xpath(
    '//img[contains(@src,"styles/ratio_unlocked_medium/public/media-image")]/@src'
)
   
# Downlaod & pair each scraped URL with relevant filenames
filenames = ("geo_sales.png", "product_mix.png")
for name, src in zip(filenames, srcs):
    img_url = urljoin(PAGE_URL, src)
    data    = requests.get(img_url).content
    Path(name).write_bytes(data)

