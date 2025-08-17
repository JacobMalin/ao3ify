
from convert import extract_pdf, dump_json, book_to_html

if __name__ == "__main__":
    TITLE = "H.I.V.E."
    AUTHOR = "Mark Walden"
    SUMMARY = "Otto Malpense may only be thirteen years old, but so far he has managed to run the orphanage where he lives, and he has come up with a plan clever enough to trick the most powerful man in the country. He is the perfect candidate to become the world's next supervillain.\nThat is why he ends up at H.I.V.E., handpicked [read: kidnapped] to become a member of the incoming class. Inside a volcano on a secluded island, Otto, along with his elite peers - the most athletic, technologically advanced, and the smartest kids in the country - will be enrolled in Villainy Studies and Stealth and Evasion. But then Otto realizes that he's entered a six-year program - where leaving is not an option. Can Otto do what has never been done before and break out of H.I.V.E.?"
    PREFACE_SKIP = 5
    POSTFACE_SKIP = 0
    
    book = extract_pdf(TITLE, AUTHOR, SUMMARY, PREFACE_SKIP, POSTFACE_SKIP)
    dump_json(book)
    book_to_html(book)