from read import make_body_html, read_all

def replace_newlines(text):
    return text.replace('\n', '<br><br>')

if __name__ == "__main__":
    TITLE = "The Dream Thieves"
    AUTHOR = "Maggie Stiefvater"
    SUMMARY = "Ronan Lynch has secrets. Some he keeps from others. Some he keeps from himself. One secret: Ronan can bring things out of his dreams. And sometimes he's not the only one who wants those things."
    PREFACE_SKIP = 4
    POSTFACE_SKIP = 6

    HTML_PATH = "books/" + TITLE + ".html"
    with open(HTML_PATH, "wb") as out:
        BOOK_PATH = "pdf/" + TITLE + ".pdf"
        template = [
            read_all("html/Template_1.html"),
            read_all("html/Template_2.html"),
            read_all("html/Template_3.html"),
            read_all("html/Template_4.html"),
            read_all("html/Template_5.html"),
            read_all("html/Template_6.html"),
        ]
        text = [
            TITLE,
            TITLE,
            AUTHOR,
            replace_newlines(SUMMARY),
            make_body_html(BOOK_PATH, PREFACE_SKIP, POSTFACE_SKIP),
        ]

        for i in range(len(text)):
            out.write(template[i])
            out.write(text[i].encode('utf8'))
        out.write(template[-1])