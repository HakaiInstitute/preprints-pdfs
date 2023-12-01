import os
from os.path import join, basename, splitext
import subprocess
from glob import glob
from shutil import copy
from random import shuffle, seed

from pyzotero import zotero

LIBRARY_ID = 5302835
LIBRARY_TYPE = "group"
USER_KEY = "ecy68xmRI6hnkvF9dyT7NcOI"

OUTPUT_DIR = 'outputs'
COLLECTION_NAME = 'API'
tag = "tag"

def get_pdfs(OUTPUT_DIR, COLLECTION_NAME):

    # Create the output directory
    path = join(OUTPUT_DIR, COLLECTION_NAME)
    os.makedirs(path, exist_ok=True)

    # Connect to Zotero
    zot = zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, USER_KEY)

    # Get the collection of interest and it's key
    collections = {c['data']['name']: c for c in zot.collections()}
    collection = collections[COLLECTION_NAME]
    key = collection['key']

    # Now get the items in the collection that have the given tag
    items = [d for d in zot.everything(zot.collection_items(key, tag=tag))]
    # items = [d for d in zot.collection_items(key, tag=tag, limit=3)]

    # Get the PDF attachment for each item and save it to the category directory
    for item in items:
        # An item's attachments
        children = [c for c in zot.children(item['key'])]

        # Just get the PDFs
        pdfs = [c for c in children
                if c['data'].get('contentType') == 'application/pdf']

        # Handle when there are no attachments
        if not children:
            print('\nMISSING DOCUMENTS {}\n'.format(item['key']))
        # Handle when there are no PDF attachments
        elif not pdfs:
            print('\nNO PDFs {}\n'.format(item['key']))
        # Handle when there is more than one PDF attachment
        elif len(pdfs) != 1:
            print('\nTOO MANY PDFs {}\n'.format(item['key']))
        # Save the PDF to the category directory
        else:
            doc = pdfs[0]
            print(doc['data']['filename'])
            zot.dump(doc['key'], '{}.pdf'.format(doc['key']), path)

get_pdfs(OUTPUT_DIR, COLLECTION_NAME)
