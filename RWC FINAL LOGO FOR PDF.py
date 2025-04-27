import requests
from pathlib import Path

#Scraping logo from wikipedia site
URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Reliance_Worldwide_Corporation_logo.svg/512px-Reliance_Worldwide_Corporation_logo.svg.png"
dest = Path("RWC_logo_Final_Copy.png")

# If we need user agent to avoid being blocked by Wikimedia - fake email
resp = requests.get(URL, headers={"User-Agent": "rwc-logo-fetcher/1.0 (finm@assignment.com)"})

#Check server response
resp.raise_for_status()
dest.write_bytes(resp.content)

#Check its the right image
from PIL import Image
img = Image.open(dest)
img.show() 

#Confirmation msg where file is saved
print(f"Logo saved to {dest}")