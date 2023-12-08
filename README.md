# README

This `pdfs` branch of `https://github.com/HakaiInstitute/preprints-pdfs` is designed to retrieve, store and serve the PDFs from Zotero Cloud for the Hakai Preprints Server:(https://preprints.hakai.org/)

It does that by a GitHub Actions Workflow:  

https://github.com/HakaiInstitute/preprints-pdfs/actions

It is some hacky Python that calls a NodeJS CLI tool for the Zotero API:

- Lists all the items in the Hakai Group Library (https://www.zotero.org/groups/5302835/hakai-institute/library) Collection for Preprints https://www.zotero.org/groups/5302835/hakai-institute/collections/FMW579SC
- Downloads each item attachment
- Adds them back to the repository branch
