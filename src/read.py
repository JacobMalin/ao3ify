import pymupdf

doc = pymupdf.open("book.pdf") # open a document
out = open("output.txt", "wb") # create a text output
out.write('<p>'.encode('utf8'))
for page in doc[6:]: # iterate the document pages
    block = page.get_text("blocks")
    for b in block:
        text = b[4]
        if text[0].isupper() or text[0] == '“':
            out.write('</p><p>'.encode('utf8'))
        out.write(text.encode('utf8')) # write text of page
out.write('</p>'.encode('utf8'))
out.close()