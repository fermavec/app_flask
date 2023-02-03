class Author:

    def __init__(self, idAuthor, lastname, authorName, birthday=None ):
        self.idAuthor = idAuthor
        self.lastname = lastname
        self.authorName = authorName
        self.birthday = birthday

    
    def fullname(self):
        return f'{self.authorName} {self.lastname}'