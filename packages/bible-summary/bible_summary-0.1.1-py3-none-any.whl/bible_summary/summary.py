import json
import importlib.resources as pkg_resources
import os

class BibleSummary:
    def __init__(self):
        self.books = self._load_books()

    def _load_books(self):
        books = {}
        data_path = pkg_resources.files('bible_summary.data')
        for file_name in data_path.iterdir():
            if file_name.suffix == '.json':
                with pkg_resources.open_text('bible_summary.data', file_name.name) as f:
                    book_data = json.load(f)
                    books.update(book_data)
        return books

    def get_summary(self, book, chapter):
        book = book.title()
        if book in self.books and chapter in self.books[book]:
            return self.books[book][chapter]
        else:
            return "Summary not available."

    def get_books(self):
        return list(self.books.keys())

    def get_chapters(self, book):
        book = book.title()
        if book in self.books:
            return list(self.books[book].keys())
        else:
            return "Book not available."
