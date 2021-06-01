from requests import get


def _get_book_cover_uri(title: str, author: str):

    req_uri = "https://www.googleapis.com/books/v1/volumes?q="

    if title is None:
        return
    req_uri += "intitle:" + title

    if author is not None:
        req_uri += "+inauthor:" + author

    response = get(req_uri).json().get("items", [])
    if len(response) > 0:
        return response[0].get("volumeInfo", {}).get("imageLinks", {}).get("thumbnail")

    return


print(_get_book_cover_uri("A Man Called Ove", "Fredrick Backman"))
