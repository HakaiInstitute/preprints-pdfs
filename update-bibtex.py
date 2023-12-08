#!/usr/bin/env python3

from pybtex.database import parse_file
from pybtex.database.input.bibtex import Parser
from pybtex.database import Entry, Person

from pybtex.plugin import find_plugin
style = find_plugin('pybtex.style.formatting', 'plain')()
backend = find_plugin('pybtex.backends', 'plaintext')()


bib_data = parse_file("./zotero.bib")


keys = bib_data.entries.keys()

for key in keys:
    # print(bib_data.entries[key].fields['file'])
    pdf = (bib_data.entries[key].fields['file'])
    pdf_stripped = pdf.replace("\\","")
    pdf_github = pdf_stripped.replace("/Users/stevevandervalk/Zotero/storage/HPW6YAKI/", "https://github.com/HakaiInstitute/preprints-pdfs/blob/pdfs/")
    bib_data.entries[key].fields['pdf'] = pdf_github
    # print(bib_data.entries[key].fields['pdf'])

print(bib_data.to_string(bib_format=""))
bib_data.to_file("updated.bib") 