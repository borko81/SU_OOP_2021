class Location:
    def __init__(self, location=''):
        if location == '':
            self.location = 'Undefine location'
        else:
            self.location = location
        self.books = []

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def add_book_to_library(self, book):
        self.books.append(book)


class TurnPage:
    def __init__(self):
        self.page = 0

    def turn_page(self, page):
        self.page = page

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page):
        self.__page = page


class Book(TurnPage):

    def __init__(self, title, author):
        super().__init__()
        self.title = title
        self.author = author
        self.location = Location('Vel')

    def find_book(self, title):
        return title in self.location.books


b = Book("King", "Stivan")
print(b.location.location)
b.location.add_book_to_library('first book')
print(b.location.books)

