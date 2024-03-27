create database connection

CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(10, 2),
    quantityInStock INT,
    type VARCHAR(50));

	CREATE TABLE Electronics(
	productId INT , 
    brand VARCHAR(255),
    warrantyPeriod INT);

	CREATE TABLE Clothing(
	productId INT ,
    size VARCHAR(50),
    color VARCHAR(50));



 CREATE TABLE users (
    userId INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE Orders (
    orderId INT PRIMARY KEY,
    userId INT,
    productId INT, 
    quantity INT,
    orderDate DATE
);




select * from users
select * from Product
select * from Electronics
select * from Clothing
select * from Orders