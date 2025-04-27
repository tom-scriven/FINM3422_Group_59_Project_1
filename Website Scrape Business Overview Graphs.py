import requests
from pathlib import Path
from PIL import Image

#RWC group at a glance

# 1) Configure your two images: (local-filename, remote-URL)
IMAGES = [
    ("geo_sales_breakdown.png",
     "https://www.rwc.com/sites/default/files/styles/"
     "ratio_unlocked_medium/public/media-image/"
     "FY24%20Geographical%20Sales%20Breakdown_1.jpg?itok=Tm2hla2y"),

    ("global_product_mix.png",
     "https://www.rwc.com/sites/default/files/styles/"
     "ratio_unlocked_medium/public/media-image/"
     "Global%20Product%20Mix_2.jpg?itok=v9F5_Xce"),
]

#If needed to avoid 403 error 
HEADERS = {
    "User-Agent": "rwc-image-fetcher/1.0 (finm@assignment.com)"
}

# 2) Loop through each, fetch + save + display to check
for filename, url in IMAGES:
    dest = Path(filename)
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    dest.write_bytes(resp.content)            # save file
    Image.open(dest).show()                   # quick pop-up check
    print(f"✔ Saved and displayed {dest}")
