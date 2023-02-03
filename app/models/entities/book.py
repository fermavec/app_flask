class Book:

    def __init__(self, isbn, bookTitle, idAuthor, publishYear=None, price=None):
        self.isbn = isbn
        self.bookTitle = bookTitle
        self.idAuthor = idAuthor
        self.publishYear = publishYear
        self.price = price