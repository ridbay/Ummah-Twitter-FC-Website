import urllib.request
import re
import json

url = "https://photos.app.goo.gl/BsKmrtvndqyobnZz6"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Google photos URLs typically start with https://lh3.googleusercontent.com/pw/
    # We can try to regex them out
    matches = re.findall(r'(https://lh3\.googleusercontent\.com/pw/[a-zA-Z0-9\-_]+)', html)
    unique_urls = list(set(matches))
    print(f"Extracted {len(unique_urls)} photos from Google Photos album")
    
    with open("photos_urls.json", "w") as f:
        json.dump(unique_urls, f)
except Exception as e:
    print(f"Error: {e}")
