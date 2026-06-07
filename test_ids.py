import urllib.request
import re

with open("src/views/Gallery.vue", "r") as f:
    content = f.read()

ids = re.findall(r"'([1][a-zA-Z0-9_-]{32})'", content)
valid_ids = []
invalid_ids = []

for id in ids:
    url = f"https://lh3.googleusercontent.com/d/{id}"
    try:
        req = urllib.request.Request(url, method='HEAD')
        res = urllib.request.urlopen(req)
        if res.status == 200:
            valid_ids.append(id)
        else:
            invalid_ids.append(id)
    except Exception as e:
        invalid_ids.append(id)
        print(f"ID {id} failed: {e}")

print(f"Valid: {len(valid_ids)}, Invalid: {len(invalid_ids)}")
print(f"Invalid IDs: {invalid_ids}")

# Let's replace the array in Gallery.vue to only contain valid_ids
new_content = re.sub(r'const imageIds = \[[^\]]+\]', f'const imageIds = {valid_ids}', content)
with open("src/views/Gallery.vue", "w") as f:
    f.write(new_content)
