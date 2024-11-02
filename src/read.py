import pymupdf
import re

book = "books/The Black Prism.pdf"
preface_end_page = 9
postface_skip_count = 4
chapter = 0

doc = pymupdf.open(book) # open a document
out = open("output.txt", "wb") # create a text output
out.write('<p>\n'.encode('utf8'))
count = 0
for page in doc[preface_end_page:-postface_skip_count]: # iterate the document pages
    block = page.get_text("blocks")
    for b in block:
        text = b[4]

        if re.fullmatch("Chapter \d+\n", text):
            count = 0
        # if " \n \n \n" in text: chapter += 1
        # text = text.replace(" \n \n \n", "</p>\0<p>\0CHAPTER {}\0</p>\0<p>".format(chapter))
        # text = text.replace(" \n \n", "\0</p>\0<p>\0")
        text = text.replace('\n', '')
        # text = text.replace('\0', '\n')
        
        if (text[0].isupper()):
            out.write('\n</p>\n'.encode('utf8')) # write text of page
            out.write('\n<p>\n'.encode('utf8')) # write text of page
        out.write(text.encode('utf8')) # write text of page
        count += 1
out.write('</p>'.encode('utf8'))
out.close()