import pymupdf
import re


def make_body_html(book_path, preface_skip, postface_skip):
    result = ""

    result += '<p>\n'

    book = pymupdf.open(book_path)  # open a book
    count = 0
    for page in book[preface_skip:-postface_skip]:  # iterate the document pages
        block = page.get_text("blocks")
        for b in block:
            text = b[4]

            if re.fullmatch("Chapter \d+\n", text):
                count = 0

            # if " \n \n \n" in text: chapter += 1
            # text = text.replace(" \n \n \n", "</p>\0<p>\0CHAPTER {}\0</p>\0<p>".format(chapter))
            # text = text.replace(" \n \n", "\0</p>\0<p>\0")
            text = text.replace('\n', ' ')
            # text = text.replace('\0', '\n')

            if (text[0].isupper()):
                result += '\n</p>\n\n<p>\n'
            result += text
            count += 1

    result += '</p>'

    return result


def read_all(path):
    with open(path, "rb") as file:
        return file.read()
