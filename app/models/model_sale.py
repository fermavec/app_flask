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