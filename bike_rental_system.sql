-- Step 1: Create Database
CREATE DATABASE BikeRentalDB;
USE BikeRentalDB;

-- Step 2: Create Tables
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address TEXT
);

CREATE TABLE Bikes (
    bike_id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(50),
    bike_type VARCHAR(50),
    status ENUM('available', 'rented', 'maintenance') DEFAULT 'available',
    price_per_hour DECIMAL(5,2)
);

CREATE TABLE Rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    bike_id INT,
    rental_start DATETIME,
    rental_end DATETIME,
    total_cost DECIMAL(7,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (bike_id) REFERENCES Bikes(bike_id)
);

-- Step 3: Insert Sample Data
INSERT INTO Customers (name, email, phone, address) VALUES
('Alice Johnson', 'alice@example.com', '123-456-7890', '123 Main St'),
('Bob Smith', 'bob@example.com', '987-654-3210', '456 Oak St');

INSERT INTO Bikes (model, bike_type, status, price_per_hour) VALUES
('Trek FX 2', 'Hybrid', 'available', 5.00),
('Giant Escape 3', 'Road', 'available', 7.50);

-- Step 4: Query Data
-- Retrieve all available bikes
SELECT * FROM Bikes WHERE status = 'available';

-- Rent a bike (update bike status)
UPDATE Bikes SET status = 'rented' WHERE bike_id = 1;

-- Retrieve rental details
SELECT r.rental_id, c.name AS customer_name, b.model AS bike_model, 
       r.rental_start, r.rental_end, r.total_cost
FROM Rentals r
JOIN Customers c ON r.customer_id = c.customer_id
JOIN Bikes b ON r.bike_id = b.bike_id;
