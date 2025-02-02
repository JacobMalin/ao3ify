from read import make_body_html, read_all

def replace_newlines(text):
    return text.replace('\n', '<br><br>')

if __name__ == "__main__":
    TITLE = "Howl's Moving Castle"
    AUTHOR = "Diana Wynne Jones"
    SUMMARY = "Sophie has the great misfortune of being the eldest of three daughters, destined to fail miserably should she ever leave home to seek her fate. But when she unwittingly attracts the ire of the Witch of the Waste, Sophie finds herself under a horrid spell that transforms her into an old lady. Her only chance at breaking it lies in the ever-moving castle in the hills: the Wizard Howl's castle.\nTo untangle the enchantment, Sophie must handle the heartless Howl, strike a bargain with a fire demon, and meet the Witch of the Waste head-on. Along the way, she discovers that there's far more to Howl—and herself—than first meets the eye.\nIn this giant jigsaw puzzle of a fantasy, people and things are never quite what they seem. Destinies are intertwined, identities exchanged, lovers confused. The Witch has placed a spell on Howl. Does the clue to breaking it lie in a famous poem? And what will happen to Sophie Hatter when she enters Howl's castle?"
    PREFACE_SKIP = 7
    POSTFACE_SKIP = 7

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
            replace_newlines(SUMMARY),
            make_body_html(BOOK_PATH, PREFACE_SKIP, POSTFACE_SKIP),
        ]

        for i in range(len(text)):
            out.write(template[i])
            out.write(text[i].encode('utf8'))
        out.write(template[-1])