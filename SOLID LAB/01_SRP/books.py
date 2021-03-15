class Library:

    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return "%s in library %s" % (book.title, self.location)
        except IndexError:
            return "This book is not in %s" % self.location

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.books):
            raise StopIteration
        result = self.books[self.n]
        self.n += 1
        return result

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


l = Library("Velingrad")
b = Book("Name of the book", "Author Name")
l.add_book(b)
for i in l:
    print(i.title)

print(l.find_book('Name of the book'))
