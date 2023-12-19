import subprocess
import json
from datetime import datetime
import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[
#         logging.FileHandler("debug.log"),
#         logging.StreamHandler()
#     ]
# )

# from loguru import logger
# logger.add("file_{time}.log")

# from pyzotero import zotero

COLLECTION_KEY = "FMW579SC"
LIBRARY_ID = "5302835"
LIBRARY_TYPE = "group"
USER_KEY = "PUHzzXnkKJieX9ugF7BbH2cf"
# this is a READONLY KEY and these PDFS are on github so...


""" 
This crap code: 
* calls a Zotero API CLI in NodeJS to list all the bibliography items in a Hakai Group Library Folder called _API_ 
* Saves the list of items to items<timestamp>.json and then iterates through each one to save each items attachment PDF to disk and name it with the item TITLE
* 
"""


# from functools import lru_cache
# @lru_cache(maxsize=None)
def get_items():
    result = subprocess.run(['./bin/zotero-cli.js', '--config', "config.toml", "items"], stdout=subprocess.PIPE)
    return result.stdout

items_in_string = get_items()
items_in_json = json.loads(items_in_string)

# timestamp = datetime.now().isoformat()
# logger.info(item_in_json)

# dump items to file
# with open('items' + timestamp +'.json', 'w', encoding='utf-8') as f:
#     json.dump(items_in_json, f, ensure_ascii=False, indent=4)

for item in items_in_json:
    key = item["key"]
    if "title" in item["data"]:
        title = item["data"]["title"]
        print(key, title)
        result = subprocess.run(['./bin/zotero-cli.js', '--config', "config.toml", "attachment", "--key", key, "--save", title], stdout=subprocess.PIPE)
        
    else:
        item_missing = f"Item {key} missing title"
        print(item_missing)
    

