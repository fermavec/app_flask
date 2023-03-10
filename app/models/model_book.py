from .entities.author import Author
from .entities.book import Book

class ModelBook:

    @classmethod
    def listing_books(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT B.isbn, B.bookTitle, A.lastname, A.authorName, B.publishYear, B.price  
                        FROM book B JOIN author A ON B.idAuthor = A.idAuthor
                        ORDER BY bookTitle ASC"""
            cursor.execute(query)
            data = cursor.fetchall()
        
            registers = []

            for row in data:
                reg_author = Author(0, row[2], row[3])
                reg_book = Book(row[0], row[1], reg_author, row[4], row[5])
                registers.append(reg_book)
            
            return registers

        except Exception as e:
            raise Exception(e)


    @classmethod
    def list_sold_books(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT sale.isbn, book.bookTitle, book.price,
                        COUNT(sale.isbn) as soldItems
                        FROM sale JOIN book 
                        ON sale.isbn = book.isbn
                        GROUP BY sale.isbn"""
            cursor.execute(query)
            data = cursor.fetchall()
        
            registers = []

            for row in data:
                reg_book = Book(row[0], row[1], None, None, row[2])
                reg_book.sold_items = int(row[3])
                registers.append(reg_book)
            
            return registers

        except Exception as e:
            raise Exception(e)