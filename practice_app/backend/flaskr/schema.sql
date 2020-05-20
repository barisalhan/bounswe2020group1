DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS comment;

CREATE TABLE Product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price FLOAT NOT NULL,
  description TEXT NOT NULL,
  location TEXT NOT NULL
);

CREATE TABLE Comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author TEXT UNIQUE NOT NULL,
  FOREIGN KEY (productID) REFERENCES Product (id),
  commentText TEXT NOT NULL
);
