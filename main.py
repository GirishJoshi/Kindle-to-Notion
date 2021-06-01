import re
from datetime import date, datetime
from logging import error
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from dateparser import parse
from notion.block import DividerBlock, HeaderBlock, TextBlock
from notion.client import NotionClient
from notion.collection import NotionDate
from pandas.io.parsers import count_empty_vals

# Notion Credentials
token = "64df8f756cbab750702dc0c1c9995ffeb2d7acb084397f5063e6ae99ce72138299972a04792721c6927f4b9ba458cfb0f0eb02c9eef5d94b05e1fc8be38d60c0702b5f0d02718a76c043e823ef3c"
pageurl = "https://www.notion.so/2b42581229294187af79396abf961399?v=4715a2b429ce4ed5a8a7fbacf588086b"

# Goodreads
goodreads_url = "https://www.goodreads.com/book/show/"

####

# Additional Data

with open("highlights.txt", "r", encoding="utf-8") as f:
    highlights = f.readlines()

while "\n" in highlights:
    highlights.remove("\n")

rating = 5

date_finished = "5/9/2019"

status = "Read"

####


# This function will populate the properties in the notion collection for the given book name.
# The book name must match from goodreads.
# This function will set: Author,
def add_book_to_notion(
    tokenv2, pageurl, bookname, bookid, highlights, rating, date_finished, status
):

    # establish connection with notion
    notion_client = NotionClient(token_v2=tokenv2)
    notion_collection_view = notion_client.get_collection_view(pageurl)

    # create a new row in the collection from the bookname, if bookname already exists then inform

    notion_collection_view_rows = notion_collection_view.collection.get_rows()

    title_exists = False
    if notion_collection_view_rows:
        for row in notion_collection_view_rows:
            if bookname == row.title:
                title_exists = True
                print(f"'{row.title}' already exists in the notion database.")

    if not title_exists:
        print(f"'{bookname}' will be added to notion database now.")
        row = notion_collection_view.collection.add_row()
        row.title = bookname

        # Updating data which came from Goodreads using Beautiful Soup

        gr_book_url = goodreads_url + str(bookid)
        soup = BeautifulSoup(urlopen(gr_book_url), "html.parser")

        ## Cover Image
        tag = soup.find("img", {"id": "coverImage"})

        try:
            row.cover = tag["src"]
        except:
            print(f"please add the cover image for '{bookname}' manually.")

        ## Author
        author = soup.find("a", {"class": "authorName"})
        author = author.find("span", {"itemprop": "name"})
        row.author = author.text

        # Updating data which came from function arguments

        ## Rating

        if rating == 5:
            row.rating = "☆☆☆☆☆"
        elif rating == 4:
            row.rating = "☆☆☆☆"
        elif rating == 3:
            row.rating = "☆☆☆"
        elif rating == 2:
            row.rating = "☆☆"
        elif rating == 3:
            row.rating = "☆"

        ## Tag

        row.tag = status

        ## Date Finished

        row.date_finished = NotionDate(parse(date_finished).date())

        ## Highlights

        # To add highlights of the book, we'll have to read the parent page.
        parent_page = notion_client.get_block(row.id)

        parent_page.children.add_new(HeaderBlock, title="Highlights")
        parent_page.children.add_new(DividerBlock)

        count = 0
        for highlight in highlights:
            print(highlight)
            parent_page.children.add_new(TextBlock, title=str(highlight))
            parent_page.children.add_new(DividerBlock)
            count += 1

        row.highlights = count


# This function will update all entry's with the divider block highlights,
# will add the review of the book form the csv file. And will update the cover image with GR URL.


def update_highlights_and_reviews(tokenv2, pageurl):

    # get the database of all the read books on goodreads
    df = pd.read_csv("girishGR.csv")
    df.drop(df[df["Exclusive Shelf"] != "read"].index, inplace=True)

    # remove special character's so it get's easy to match book names from notion database
    df.Title = df.Title.str.replace("[^A-Za-z0-9]+", " ", regex=True)

    # establish connection with notion
    notion_client = NotionClient(token_v2=tokenv2)
    notion_collection_view = notion_client.get_collection_view(pageurl)
    notion_collection_view_rows = notion_collection_view.collection.get_rows()

    count = 0
    rcount = 0

    for row in notion_collection_view_rows:

        # if row.updated is set yes, then the code will not update that book details.
        if row.updated == "Yes":
            print(f"{row.title} is already updated.")
            count += 1
            continue

        count += 1

        highlights = []

        print(f"Inside {row.title}")

        parent_page = notion_client.get_block(row.id)

        # Remove all the old blocks of the page, and save all the text blocks in highlights list.
        for all_blocks in parent_page.children:

            try:
                highlights.append(all_blocks.title)
            except:
                pass

            all_blocks.remove()

        # Strip specail characters to match titles with csv database.
        check_temp = re.sub("[^A-Za-z0-9]+", " ", row.title)

        # If the review exists in the csv database for the current book, update the review in page.
        if bool(df[df["Title"] == check_temp]["My Review"].any()):

            review = df[df["Title"] == check_temp]["My Review"].item()

            parent_page.children.add_new(HeaderBlock, title="Review")
            parent_page.children.add_new(DividerBlock)
            parent_page.children.add_new(TextBlock, title=str(review))
            parent_page.children.add_new(DividerBlock)

            rcount += 1
            print(f"Review of {row.title} added: {rcount}/81")

        # Add the removed highlights again with the divider block.
        parent_page.children.add_new(HeaderBlock, title="Highlights")
        parent_page.children.add_new(DividerBlock)

        for highlight in highlights:
            parent_page.children.add_new(TextBlock, title=str(highlight))
            parent_page.children.add_new(DividerBlock)

        row.updated = "Yes"
        print(f"{count}/202 books done.")


def populate_read_dates(tokenv2, pageurl):

    # get the database of all the read books on goodreads
    df = pd.read_csv("girishGR.csv")
    df.drop(df[df["Exclusive Shelf"] != "read"].index, inplace=True)

    # remove special character's so it get's easy to match book names from notion database
    df.Title = df.Title.str.replace("[^A-Za-z0-9]+", " ", regex=True)

    # establish connection with notion
    notion_client = NotionClient(token_v2=tokenv2)
    notion_collection_view = notion_client.get_collection_view(pageurl)

    notion_collection_view_rows = notion_collection_view.collection.get_rows()

    count = 0
    rcount = 0

    for row in notion_collection_view_rows:

        if row.tag == "Read":
            rcount += 1

            # Strip specail characters to match titles with csv database.
            check_temp = re.sub("[^A-Za-z0-9]+", " ", row.title)

            # If the review exists in the csv database for the current book, update the review in page.
            try:
                if bool(df[df["Title"] == check_temp]["Date Read"].any()):

                    date = df[df["Title"] == check_temp]["Date Read"].item()
                    print(f"{row.title} was read on {date}")
                    new_date = datetime.strptime(date, "%d/%m/%y").strftime("%Y-%m-%d")
                    print(NotionDate(parse(new_date)))
                    row.date_finished = NotionDate(parse(new_date).date())
                    count += 1

            except:
                # print(e)
                print(f"Some issue with {row.title}")

    print(f"R: {rcount} C:{count}")


def book_cover_and_genres(tokenv2, pageurl):

    # get the database of all the read books on goodreads
    df = pd.read_csv("girishGR.csv")
    df.drop(df[df["Exclusive Shelf"] != "read"].index, inplace=True)

    # remove special character's so it get's easy to match book names from notion database
    df.Title = df.Title.str.replace("[^A-Za-z0-9]+", " ", regex=True)

    # establish connection with notion
    notion_client = NotionClient(token_v2=tokenv2)
    notion_collection_view = notion_client.get_collection_view(pageurl)

    notion_collection_view_rows = notion_collection_view.collection.get_rows()

    count = 0
    rcount = 0

    for row in notion_collection_view_rows:

        if row.updated == "No":
            print(f"{row.title} is already updated for cover and genre.")
            continue

        rcount += 1
        # Strip specail characters to match titles with csv database.
        check_temp = re.sub("[^A-Za-z0-9]+", " ", row.title)

        try:
            if bool(df[df["Title"] == check_temp]["Book Id"].any()):

                print(f"Inside: {row.title}")

                b_ID = df[df["Title"] == check_temp]["Book Id"].item()
                print(f"{row.title} has book id: {b_ID}")

                gr_book_url = goodreads_url + str(b_ID)
                soup = BeautifulSoup(urlopen(gr_book_url), "html.parser")

                ## Cover Image
                tag = soup.find("img", {"id": "coverImage"})

                try:
                    row.cover = tag["src"]
                    # print(tag["src"])
                except:
                    print(f"please add the cover image for '{row.title}' manually.")

                ## Genre
                genre = soup.find("div", {"class": "elementList"})
                genre = genre.find("a", {"class": "bookPageGenreLink"})
                # genre = genre.find_all("div", {"class": "elementList"})
                if genre == None:
                    print(f"{row.title} is probably a fiction.")
                    row.genre = "Fiction"
                else:
                    row.genre = genre.text
                    print(genre.text)

                # row.author = author.text
                count += 1
                row.updated == "No"
        except:
            # print(e)
            print(f"Some issue with {row.title}")

        print(f"completed {count} books")


"""
add_book_to_notion(
    token,
    pageurl,
    "How to Day Trade for a Living: A Beginner's Guide to Trading Tools and Tactics, Money Management, Discipline and Trading Psychology",
    "31808862",
    highlights,
    rating,
    date_finished,
    status,
)
"""

# update_highlights_and_reviews(token, pageurl)
# populate_read_dates(token, pageurl)
book_cover_and_genres(token, pageurl)
print("over")
