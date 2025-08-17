import pymupdf
import re

from book import Chapter

def extract_chapters(book_path, preface_skip, postface_skip):
    book = pymupdf.open(book_path)  # open a book
    
    if postface_skip == 0:
        book = book[preface_skip:]
    else:
        book = book[preface_skip:-postface_skip]

    chapters_text = []
    chapter_text = ""
    chapter_name = ""
    for page in book:  # iterate the document pages
        block = page.get_text("blocks") # pyright: ignore[reportAttributeAccessIssue]
        for b in block:
            text = b[4]
            
            # Skip blocks that are just a page number
            if text.strip().isdigit():
                continue
                
            # Match chapter
            match = re.search(r"(chapter)\s+(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\b\s+?", text, re.IGNORECASE)
            if match:
                before = text[:match.start()]
                after = text[match.end():]
                
                chapter_text += before

                if chapter_text != "":
                    chapters_text.append((chapter_name, chapter_text))
                    chapter_text = ""
                chapter_name = match.group(0).strip()
                
                chapter_text = after
                continue
                
            chapter_text += text

    chapters_text.append((chapter_name, chapter_text))

    CAPTURE_ONE = r"(\.|’)"
    CAPTURE_TWO = r"(‘|[A-Z])"
    FULL_CAPTURE = CAPTURE_ONE + r"\s+\n" + CAPTURE_TWO
    chapters = []
    
    for chapter_name, chapter in chapters_text:
        regex_split_paragraphs = re.split(FULL_CAPTURE, chapter)
        regex_split_paragraphs = [p.replace('\n', '').strip() for p in regex_split_paragraphs]
        
        paragraphs = []
        hold_over = ""
        for paragraph in regex_split_paragraphs:
            if re.fullmatch(CAPTURE_ONE, paragraph):
                paragraphs[-1] += paragraph
            elif re.fullmatch(CAPTURE_TWO, paragraph):
                hold_over = paragraph
            else:
                paragraphs.append(hold_over + paragraph)
                hold_over = ""
            
        chapters.append(Chapter(paragraphs=paragraphs, title=chapter_name))


    return chapters


def read_all(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
