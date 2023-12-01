from pyzotero import zotero
# https://github.com/urschrei/pyzotero

library_id = 5302835
library_type = "group"
api_key = "ecy68xmRI6hnkvF9dyT7NcOI"

zot = zotero.Zotero(library_id, library_type, api_key)
items = zot.items()
results = zot.everything(zot.top())

group_collection_only = zot.collection_items("FMW579SC")

print(group_collection_only)
