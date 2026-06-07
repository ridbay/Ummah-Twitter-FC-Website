import json
import re

with open("all_drive_ids.json", "r") as f:
    ids = json.load(f)

# Format the ids array nicely as JS code
ids_str = "[\n  " + ",\n  ".join(f"'{id}'" for id in ids) + "\n]"

with open("src/views/Gallery.vue", "r") as f:
    content = f.read()

# Replace the const imageIds = [...] block
new_content = re.sub(
    r'const imageIds = \[[^\]]*\]',
    f'const imageIds = {ids_str}',
    content,
    flags=re.MULTILINE | re.DOTALL
)

with open("src/views/Gallery.vue", "w") as f:
    f.write(new_content)

print("Updated Gallery.vue with 737 IDs")
