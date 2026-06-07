import urllib.request
import re

url = "https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Search for all 33-char alphanumeric strings in the HTML
    matches = re.findall(r'([a-zA-Z0-9_-]{33})', html)
    # Filter for typical google drive ID format (usually starts with 1)
    ids = list(set([m for m in matches if m.startswith('1')]))
    print(f"Found IDs: {ids}")
except Exception as e:
    print(f"Error: {e}")
