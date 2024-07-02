import os
import json

class BibleSummary:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.books = self._load_books()

    def _load_books(self):
        books = {}
        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('.json'):
                with open(os.path.join(self.data_dir, file_name), 'r', encoding='utf-8') as f:
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
