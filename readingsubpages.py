from datetime import datetime
from typing import Dict, List, Tuple

from dateparser import parse
from notion.block import TextBlock
from notion.client import NotionClient
from notion.collection import NotionDate
from pkg_resources import register_namespace_handler
from requests import get

from bs4 import BeautifulSoup
from urllib.request import urlopen

import pandas as pd

df = pd.read_csv("girishGR.csv")

readbooks = []
filename = "read.txt"
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        readbooks.append(line.strip())
# print(readbooks)


# print(len(grdb.index))
# print(grdb[grdb["My Rating"] == 0])

# df.drop(df[df["My Rating"] == 0].index, inplace=True)
# df.drop(df[df.Title == "The Last Mughal: The Fall of a Dynasty: Delhi, 1857"].index,inplace=True,)

df.set_index("Title", inplace=True)

# result = df.loc["A Gentleman in Moscow"]["Book Id"]
# print(result)

# print(grdb["Title"])

goodreads_url = "https://www.goodreads.com/book/show/"

token = "64df8f756cbab750702dc0c1c9995ffeb2d7acb084397f5063e6ae99ce72138299972a04792721c6927f4b9ba458cfb0f0eb02c9eef5d94b05e1fc8be38d60c0702b5f0d02718a76c043e823ef3c"
pageurl = "https://www.notion.so/2b42581229294187af79396abf961399?v=4715a2b429ce4ed5a8a7fbacf588086b"


def readsubpages(tokenv2, pageurl):

    # Setup Notion & Python

    notion_client = NotionClient(token_v2=tokenv2)
    notion_collection_view = notion_client.get_collection_view(pageurl)

    # Fetching the database. Collection is a database in notion.
    notion_collection_view_rows = notion_collection_view.collection.get_rows()

    count = 0
    i = 0

    # traversing through each row of the database/collection
    for row in notion_collection_view_rows:

        global readbooks

        # print(row.title)

        if row.title in readbooks and row.tag == "Read":
            print(f"Notion: {row.title} in Goodreads")
            readbooks.remove(row.title)
        elif row.tag == "Read":
            print(f"Not on Goodreads List: {row.title}")

            # print row.id & row.title
            # print(row)

            # you can now do row.property to access the properties of your collection.

            # To get the children (subpages) of the current page. This code fetches the blocks (text chunks)
            # inside the current page. Useful if you want to change the content of each page/card.
            # sub_page = notion_client.get_block(row.id)

            # for all_blocks in sub_page.children:
            # print(all_blocks.title)
            # I used this pieace of code to count the number of highlights for each book.
            # In future I will use this loop to add my GR Reviews and to improve the content of each book.
            # pass

            # For testing the code at a particular property. Write if True incase you want to loop over
            # all the rows. Since the database is huge, it reduces the time to debug the code.

            # print(row.title)

            # if row.title in df.index:
            # print(df.index[i])
            # print(row.title)
            # i += 1

            # if df.index.str.contains(row.title).any():

            """
            if row.tag == "Read":
                try:
                    titledb = df.loc[df.index.str.contains(row.title)]
                    r = titledb["My Rating"][0]

                    if r == 5:
                        row.rating = "☆☆☆☆☆"
                    elif r == 4:
                        row.rating = "☆☆☆☆"
                    elif r == 3:
                        row.rating = "☆☆☆"

                    # row.date_read = NotionDate(parse(titledb["Date Read"][0]).date())
                    # print(parse(titledb["Date Read"][0]).date())
                except:
                    print(f"{row.title} not updated on GR.")

            # print(titledb["Date Read"])
            """
            """
            id = df.loc[row.title]["Book Id"]
            url_open = goodreads_url + str(id)
            soup = BeautifulSoup(urlopen(url_open), "html.parser")
            tag = soup.find("img", {"id": "coverImage"})

            try:
                row.cover = tag["src"]
            except:
                print("url not found")

            print(id)
            """

            # count += 1
            # print(row.cover)
            # print(row.tag)
            # print(row.highlights)
            # print(len(sub_page.children))
            # print("----------------------------")
            # row.highlights = len(sub_page.children)

            # else:
            # print(row.title)
            # titledb = df.loc[df.index.str.contains(row.title)]
            # print(row.title)

            # print("----------------------------")

    print(count)


readsubpages(token, pageurl)

print(readbooks)
print("return 0")
