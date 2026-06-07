import urllib.request
import re
import json

url = "https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-"
# gdown does this internally: it makes an API request using some undocumented endpoints or just parses HTML.
# But we can try to extract the API key from the HTML and make a request to the drive API to get all items?
# Let's just download the folder with gdown into a temp dir and then we don't even need IDs if we serve them locally? 
# No, the user wants the IDs.
import gdown

try:
    # Instead of full download, we can use a custom parser or just let gdown fetch it.
    # Actually gdown's folder download is robust.
    # Let's inspect gdown's code for folder parsing:
    import gdown.parse_url
    import gdown.download_folder
    # We can patch gdown.download to just print the url/id and return
    original_download = gdown.download
    
    all_ids = []
    
    def mock_download(url, output, quiet, fuzzy, resume, speed, use_cookies, id):
        if id:
            all_ids.append(id)
        elif url:
            m = re.search(r'id=([a-zA-Z0-9_-]+)', url)
            if m:
                all_ids.append(m.group(1))
            else:
                m = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
                if m:
                    all_ids.append(m.group(1))
        return output

    gdown.download = mock_download
    gdown.download_folder(url, quiet=True, use_cookies=False)
    
    print(f"Total IDs extracted by gdown: {len(all_ids)}")
    print(json.dumps(list(set(all_ids))))
except Exception as e:
    print(e)
