import json
import re

with open("photos_urls.json", "r") as f:
    new_urls = json.load(f)

with open("src/views/Gallery.vue", "r") as f:
    content = f.read()

# Extract the existing array contents
match = re.search(r'const imageIds = \[([^\]]*)\]', content)
if not match:
    print("Could not find imageIds array")
    exit(1)

existing_items = match.group(1).strip()

# Create string of new items
new_items_str = ",\n  ".join(f"'{url}'" for url in new_urls)

if existing_items:
    updated_items = existing_items + ",\n  " + new_items_str
else:
    updated_items = new_items_str

new_content = content[:match.start()] + f"const imageIds = [\n  {updated_items}\n]" + content[match.end():]

# Also update the getImageUrl function
# function getImageUrl(id) {
#   return `https://lh3.googleusercontent.com/d/${id}`
# }
# into:
# function getImageUrl(id) {
#   if (id.startsWith('http')) return `${id}=w1200`;
#   return `https://lh3.googleusercontent.com/d/${id}`;
# }

new_content = re.sub(
    r'function getImageUrl\(id\) \{\s*return `https://lh3\.googleusercontent\.com/d/\$\{id\}`\s*\}',
    "function getImageUrl(id) {\n  if (id.startsWith('http')) return `${id}=w1200`;\n  return `https://lh3.googleusercontent.com/d/${id}`;\n}",
    new_content
)

with open("src/views/Gallery.vue", "w") as f:
    f.write(new_content)

print(f"Appended {len(new_urls)} URLs to Gallery.vue")
