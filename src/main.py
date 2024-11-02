from read import make_body_html, read_all

if __name__ == "__main__":
    TITLE = "The Black Prism"
    AUTHOR = "Brent Weeks"
    SUMMARY = "Guile is the Prism. He is high priest and emperor, a man whose power, wit, and charm are all that preserves a tenuous peace. Yet Prisms never last, and Guile knows exactly how long he has left to live. When Guile discovers he has a son, born in a far kingdom after the war that put him in power, he must decide how much he's willing to pay to protect a secret that could tear his world apart."
    PREFACE_SKIP = 9
    POSTFACE_SKIP = 4

    HTML_PATH = "books/" + TITLE + ".html"
    with open(HTML_PATH, "wb") as out:
        BOOK_PATH = "books/" + TITLE + ".pdf"
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
            SUMMARY,
            make_body_html(BOOK_PATH, PREFACE_SKIP, POSTFACE_SKIP),
        ]

        for i in range(len(text)):
            out.write(template[i])
            out.write(text[i].encode('utf8'))
        out.write(template[-1])
