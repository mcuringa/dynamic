# Library.py


class Book(object):
    """Create a Book class with basic bibliographic information"""
    
    def __init__(self, title, author, year, ISBN=""):
        self.title = title
        self.author = author
        self.year = year
        self.ISBN = ISBN
        self.author.AddBook(self)

    def __str__(self):
        """A string representation of this Book"""
        return "{} ({})".format(self.title,self.year)


class Author(object):
    """The author of a book"""
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.books = []
    
    def AddBook(self, book):
        book.author = self
        self.books.append(book)
    


def main():
    
    joyce = Author("James","Joyce")
    
    dubliners = Book("Dubliners", joyce, 1914)
    portrait = Book("Portrait of the Artist as a Young Man", joyce, 1916)
    ulysses = Book("Ulysses", joyce, 1922)
    finnegan = Book("Finnegans Wake", joyce, 1939)

    for b in joyce.books:
        print(b)


if __name__ == '__main__':
    main()
