from shutil import rmtree
from pathlib import Path

# run this to clear caches (locally saved responses from Groq)

CACHE_FOLDER = "./static/caches"
if CACHE_FOLDER == "./static/caches":
    rmtree(CACHE_FOLDER)
else:
    print("This isn't the correct cache folder.")
Path(CACHE_FOLDER).mkdir(exist_ok=True)