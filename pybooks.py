#!/usr/bin/env python3

import sys
from pathlib import Path
import glob
import os
import asyncio

import utils.search
from remove_bad_chars import remove_bad_chars
from rename import rename

async def main():
    #initiates the api session
    s = utils.search.Search()

    # defines first command line argument as directory to use
    path = sys.argv[1]

    #change working path to directory defined in the first argument
    os.chdir(path)
    path = Path(".")
    glob_path = path.glob("*pdf") # set it work on .pdf files only

    #runs for every file in the directory 
    for filename in glob_path:
        print(filename)
        query = await remove_bad_chars(filename)

        item = await s.get_item(query)

        title = await s.get_title(item)
        authors = await s.get_authors(item)

        new_filename = authors + " - " + title + ".pdf"

        await rename(filename, new_filename)

if __name__ == "__main__": 
    asyncio.run(main())