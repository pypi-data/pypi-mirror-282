import json
import pkg_resources

class BibleSummary:
    def __init__(self):
        self.books = self._load_books()

    def _load_books(self):
        books = {}
        resource_package = __name__
        resource_path = 'data/'  # Do not use os.path.join()

        for resource in pkg_resources.resource_listdir(resource_package, resource_path):
            if resource.endswith('.json'):
                full_path = pkg_resources.resource_filename(resource_package, f'{resource_path}{resource}')
                with open(full_path, 'r', encoding='utf-8') as f:
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
