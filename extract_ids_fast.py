import gdown
import json

url = "https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-"
try:
    files = gdown.download_folder(url, quiet=True, skip_download=True)
    all_ids = [f.id for f in files if f.id]
    print(f"Total IDs extracted: {len(all_ids)}")
    
    with open("all_drive_ids.json", "w") as f:
        json.dump(all_ids, f)
except Exception as e:
    print(e)
