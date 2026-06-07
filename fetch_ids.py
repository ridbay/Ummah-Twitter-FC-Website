import gdown

url = "https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-"
try:
    res = gdown.download_folder(url, quiet=True, use_cookies=False, remaining_ok=True)
    # wait, download_folder returns a list of filenames downloaded, but not IDs.
except Exception as e:
    print(e)
