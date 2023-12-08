#!/usr/bin/env python3

import re

# pattern = r'file = "/Users/stevevandervalk/Zotero/storage/[^/]*/'
# match = re.search(pattern, your_string)

# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")

input_file = "zotero.bib"

output_file = "github.bib"

oldString = "file = {/Users/stevevandervalk/Zotero/storage/"

newString = "pdf = {https://github.com/HakaiInstitute/preprints-pdfs/blob/pdfs/"

def replaceAll(input_file, output_file):
    with open(input_file) as infile,  open(output_file, 'w') as outfile:
        for line in infile:
            pattern = r'file = "{/Users/stevevandervalk/Zotero/storage/[^/]*/[^/]*/'
            match = re.search(pattern, line)

            if match:
                print("Match found:", match.group())
                outfile.write(line.re.sub(pattern, newString))
            else:
                print("No match found.")
            


replaceAll(input_file, output_file)