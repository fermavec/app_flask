import datetime

class Sale:

    def __init__(self, uuid, isbn, idUser, transactionDate):
        self.uuid = uuid
        self.isbn = isbn
        self.idUser = idUser
        self.transactionDate = transactionDate

    
    def format_date(self):
        return datetime.datetime.strftime(self.transactionDate, '%Y/%d/%m - %H:%M:%S')