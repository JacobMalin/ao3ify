from book import Book
from extract_pdf import extract_chapters, read_all
import json
import os

CHAPTER_BY_CHAPTER = '<li class="chapter bychapter"><a href="{}">Chapter by Chapter</a></li>'
CHAPTER_ENTIRE = '<li class="chapter entire"><a href="{}">Entire Work</a></li>'
PREVIOUS_CHAPTER = '<li class="chapter previous"><a href="{}#workskin">← Previous Chapter</a></li>'
NEXT_CHAPTER = '<li class="chapter next"><a href="{}#workskin">Next Chapter →</a></li>'

TITLE_TAG = "<!--TITLE-->"
FILES_PATH_TAG = "<!--FILES_PATH-->"
WORK_ACTIONS_TAG = "<!--WORK_ACTIONS-->"
AUTHOR_TAG = "<!--AUTHOR-->"
SUMMARY_MODULE_TAG = "<!--SUMMARY_MODULE-->"
CHAPTERS_TAG = "<!--CHAPTERS-->"
NAVIGATION_ACTIONS_TAG = "<!--NAVIGATION_ACTIONS-->"

SUMMARY_TAG = "<!--SUMMARY-->"

CHAPTER_NUMBER_TAG = "<!--CHAPTER_NUMBER-->"
CHAPTER_TITLE_TAG = "<!--CHAPTER_TITLE-->"
CHAPTER_TEXT_TAG = "<!--CHAPTER_TEXT-->"

ENTIRE_WORK = 0

def replace_newlines(text):
    return text.replace('\n', '<br><br>')

def extract_pdf(title, author, summary, preface_skip, postface_skip):
    book_path = f"pdf/{title}.pdf"
    chapters = extract_chapters(book_path, preface_skip, postface_skip)
    
    return Book(
        title=title,
        author=author,
        chapters=chapters,
        summary=summary
    )

def dump_json(book):
    output_path = os.path.join("json", f"{book.title}.json")

    # Save output to json file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2, default=vars)

def book_to_html(book):
    make_single_html(book, ENTIRE_WORK)

    for i in range(len(book.chapters)):
        make_single_html(book, i + 1)

def make_single_html(book, chapter_num):
    book_folder = book.title
    if book.title[-1] == ".":
        book_folder = book.title[:-1]

    template = read_all("html/Work.html")

    template = template.replace(TITLE_TAG, book.title)
    template = template.replace(AUTHOR_TAG, book.author)
    
    if chapter_num == ENTIRE_WORK or chapter_num == 1:
        summary_template = read_all("html/Summary_module.html")
        summary_template = summary_template.replace(SUMMARY_TAG, replace_newlines(book.summary))
        template = template.replace(SUMMARY_MODULE_TAG, summary_template)

    if chapter_num == ENTIRE_WORK:
        html_path = os.path.join("books", book_folder, f"entire_work.html")
        template = template.replace(FILES_PATH_TAG, f"..")
        
        template = template.replace(WORK_ACTIONS_TAG, CHAPTER_BY_CHAPTER.format(f"chapters/1.html"))
    else:
        html_path = os.path.join("books", book_folder, "chapters", f"{chapter_num}.html")
        template = template.replace(FILES_PATH_TAG, f"../..")
        
        work_actions = []
        navigation_actions = []
        
        work_actions.append(CHAPTER_ENTIRE.format(f"../entire_work.html"))
        if chapter_num > 1:
            work_actions.append(PREVIOUS_CHAPTER.format(f"{chapter_num - 1}.html"))
            navigation_actions.append(PREVIOUS_CHAPTER.format(f"{chapter_num - 1}.html"))
        if chapter_num < len(book.chapters):
            work_actions.append(NEXT_CHAPTER.format(f"{chapter_num + 1}.html"))
            navigation_actions.append(NEXT_CHAPTER.format(f"{chapter_num + 1}.html"))
        
        template = template.replace(WORK_ACTIONS_TAG, "\n".join(work_actions))
        template = template.replace(NAVIGATION_ACTIONS_TAG, "\n".join(navigation_actions))

    chapters = []
    if chapter_num == ENTIRE_WORK:
        for i in range(chapter_num, len(book.chapters)):
            chapter_template = make_chapter(book, i + 1)
            chapters.append(chapter_template)
    else:
        chapter_template = make_chapter(book, chapter_num)
        chapters.append(chapter_template)

    template = template.replace(CHAPTERS_TAG, "\n".join(chapters))

    with open(html_path, "w", encoding="utf-8") as out:
        out.write(template)

def make_chapter(book, chapter_num):
    chapter_template = read_all("html/Chapter.html")
    
    chapter_template = chapter_template.replace(CHAPTER_NUMBER_TAG, str(chapter_num))
    chapter_template = chapter_template.replace(CHAPTER_TITLE_TAG, book.chapters[chapter_num - 1].title)
    chapter_template = chapter_template.replace(CHAPTER_TEXT_TAG, "<p>" + "</p>\n<p>".join(book.chapters[chapter_num - 1].paragraphs) + "</p>")

    return chapter_template