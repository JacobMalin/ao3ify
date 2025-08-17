from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Chapter:
    paragraphs: List[str]
    title: Optional[str] = None

@dataclass
class Book:
    title: str
    author: str
    chapters: List[Chapter]
    summary: Optional[str] = None