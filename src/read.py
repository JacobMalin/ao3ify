import pymupdf
import re

book = "books/The Raven Boys.pdf"
preface_end_page = 5
chapter = 0

doc = pymupdf.open(book) # open a document
out = open("output.txt", "wb") # create a text output
out.write('<p>'.encode('utf8'))
for page in doc[preface_end_page:]: # iterate the document pages
    block = page.get_text("blocks")
    for b in block:
        text = b[4]

        if re.fullmatch("\d+ \n", text): continue
        if " \n \n \n" in text: chapter += 1
        text = text.replace(" \n \n \n", "</p>\0<p>\0CHAPTER {}\0</p>\0<p>".format(chapter))
        text = text.replace(" \n \n", "\0</p>\0<p>\0")
        text = text.replace('\n', '')
        text = text.replace('\0', '\n')

        out.write(text.encode('utf8')) # write text of page
out.write('</p>'.encode('utf8'))
out.close()