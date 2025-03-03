from read import make_body_html, read_all

def replace_newlines(text):
    return text.replace('\n', '<br><br>')

if __name__ == "__main__":
    TITLE = "Royal Assassin"
    AUTHOR = "Robin Hobb"
    SUMMARY = "Fitz has barely survived his first hazardous mission as king’s assassin. Battered and bitter, he vows to abandon his oath to King Shrewd, remaining in the distant mountains. But love and events of terrible urgency draw him back to the court at Buckkeep, and into the deadly intrigues of the royal family.\nRenewing their vicious attacks on the coast, the Red-Ship Raiders leave burned-out villages and demented victims in their wake. The kingdom is also under assault from within, as treachery threatens the throne of the ailing king. In this time of great danger, the fate of the kingdom may rest in Fitz’s hands—and his role in its salvation may require the ultimate sacrifice."
    PREFACE_SKIP = 4
    POSTFACE_SKIP = 1

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