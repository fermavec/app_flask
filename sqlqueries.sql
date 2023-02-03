USE mavec_store;

SHOW TABLES; 

DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS user_access;

CREATE TABLE user_access (
  idUserAccess INT UNSIGNED NOT NULL AUTO_INCREMENT,
  accessType VARCHAR(255) NOT NULL,
  PRIMARY KEY (idUserAccess)
) DEFAULT CHARSET=utf8mb4;

DESCRIBE user_access;

CREATE TABLE user (
  idUser INT UNSIGNED NOT NULL AUTO_INCREMENT,
  userName VARCHAR(255) NOT NULL,
  userPass CHAR(60) NOT NULL,
  idUserAccess INT UNSIGNED NOT NULL,
  PRIMARY KEY (idUser),
  FOREIGN KEY (idUserAccess) REFERENCES user_access(idUserAccess)
) DEFAULT CHARSET=utf8mb4;

DESCRIBE user;

CREATE TABLE author (
  idAuthor INT UNSIGNED NOT NULL AUTO_INCREMENT,
  lastname VARCHAR(255) NOT NULL,
  authorName VARCHAR(255) NOT NULL,
  birthday DATETIME,
  PRIMARY KEY (idAuthor)
) DEFAULT CHARSET=utf8mb4;

SHOW TABLES;

DESCRIBE author;

CREATE TABLE book (
	isbn VARCHAR(16) NOT NULL,
    bookTitle VARCHAR(255) NOT NULL,
    idAuthor INT UNSIGNED NOT NULL,
    publishYear YEAR,
    price DECIMAL(3, 0) NOT NULL,
    PRIMARY KEY (isbn),
    FOREIGN KEY (idAuthor) REFERENCES author(idAuthor)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE sale (
  uuid CHAR(36) NOT NULL PRIMARY KEY,
  isbn VARCHAR(16) NOT NULL,
  idUser INT UNSIGNED NOT NULL,
  transactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (idUser) REFERENCES user(idUser),
  FOREIGN KEY (isbn) REFERENCES book(isbn)
) DEFAULT CHARSET=utf8mb4;

SHOW TABLES;


/* Agregando valores a las tablas */
INSERT INTO user_access (accessType)
VALUES ('admin'), ('client');

SELECT * FROM user_access;

/*los siguientes valores son ficticios*/
INSERT INTO author (lastname, authorName, birthday)
VALUES
("King", "Stephen", "1947-09-21"),
("Rowling", "J.K.", "1965-07-31"),
("Martin", "George R.R.", "1948-09-20"),
("Gaiman", "Neil", "1960-11-10"),
("Perez-Reverte", "Arturo", "1951-11-25"),
("Eco", "Umberto", "1932-01-05"),
("Asimov", "Isaac", "1920-01-02"),
("Wells", "H.G.", "1866-09-21"),
("Orwell", "George", "1903-06-25"),
("Bradbury", "Ray", "1920-08-22"),
("Brontë", "Charlotte", "1816-04-21"),
("Brontë", "Emily", "1818-07-30"),
("Austen", "Jane", "1775-12-16"),
("Wilde", "Oscar", "1854-10-16"),
("Shakespeare", "William", "1564-04-23"),
("Tolkien", "J.R.R.", "1892-01-03"),
("Heinlein", "Robert A.", "1907-07-07"),
("Clarke", "Arthur C.", "1917-12-16"),
("Dick", "Philip K.", "1928-12-16"),
("Gibson", "William", "1948-03-17"),
("Atwood", "Margaret", "1939-11-18"),
("Butler", "Octavia", "1947-06-22"),
("Morrison", "Toni", "1931-02-18"),
("Angelou", "Maya", "1928-04-04");

SELECT * FROM author;


INSERT INTO book (isbn, bookTitle, idAuthor, publishYear, price)
VALUES
("0-672-31399-7", "The Shining", 1, 1977, 9.99),
("0-316-01118-4", "Carrie", 1, 1974, 12.99),
("0-345-53550-2", "The Stand", 1, 1978, 15.99),
("0-7528-5799-8", "Harry Potter and the Philosopher's Stone", 2, 1997, 20.00),
("0-7528-5797-1", "Harry Potter and the Chamber of Secrets", 2, 1998, 20.00),
("0-7528-5796-3", "Harry Potter and the Prisoner of Azkaban", 2, 1999, 20.00),
("0-5535-0720-7", "A Game of Thrones", 3, 1996, 25.00),
("0-5535-9024-8", "A Clash of Kings", 3, 1998, 25.00),
("0-5535-9027-2", "A Storm of Swords", 3, 2000, 25.00),
("0-06-051519-9", "American Gods", 4, 2001, 19.99),
("0-06-780966-6", "Anansi Boys", 4, 2005, 19.99),
("0-316-01062-2", "The Name of the Rose", 5, 1980, 17.99),
("0-316-01064-9", "Foucault's Pendulum", 5, 1988, 17.99),
("0-316-16554-0", "I, Robot", 6, 1950, 14.99),
("0-06-000254-2", "The Time Machine", 7, 1895, 9.99),
("0-4515-2658-9", "1984", 8, 1949, 12.99),
("0-394-75582-X", "Fahrenheit 451", 9, 1953, 14.99),
("0-06-051517-2", "Good Omens", 10, 1990, 20.00),
("0-316-08421-9", "Pride and Prejudice", 11, 1813, 15.99),
("0-679-40937-3", "Beloved", 12, 1987, 20.00),
("0-679-76827-7", "Sula", 12, 1973, 20.00),
("0-679-76727-1", "Jazz", 12, 1992, 20.00),
("0-575-07323-0", "The Handmaid's Tale", 13, 1985, 22.99),
("0-14-014834-2", "The Blind Assassin", 13, 2000, 22.99);

SELECT * FROM book;