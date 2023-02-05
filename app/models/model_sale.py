from .entities.book import Book
from .entities.sale import Sale

class ModelSale:
    
    @classmethod
    def register(self, db, purchase):
        try:
            cursor = db.connection.cursor()
            query = "INSERT INTO sale (uuid, isbn, idUser, transactionDate) VALUES (uuid(), '{0}', {1}, CURRENT_TIMESTAMP);".format(purchase.isbn, purchase.idUser)
            cursor.execute(query)
            db.connection.commit()
            return True
        except Exception as e:
            raise Exception(e)

    
    @classmethod
    def list_user_items(self, db, user):
        try:
            cursor = db.connection.cursor()
            query = "SELECT sale.transactionDate, book.isbn, book.bookTitle, book.price FROM sale JOIN book ON sale.isbn=book.isbn WHERE sale.idUser={0}".format(user.idUser)
            cursor.execute(query)
            data = cursor.fetchall()
            purchases=[]

            for row in data:
                bks = Book(row[1], row[2], None, None, row[3])
                pchs = Sale(None, bks, user, str(row[0]))
                purchases.append(pchs)
            return purchases
        except Exception as e:
            raise Exception(e)    