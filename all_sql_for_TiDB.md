```
CREATE DATABASE coffee;
USE coffee;

SET time_zone = 'Asia/Ho_Chi_Minh';
CREATE TABLE IF NOT EXISTS category (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
);

CREATE TABLE IF NOT EXISTS drink (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
price INT DEFAULT 0,
category INT,
FOREIGN KEY (category) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS
  `employee` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `position` INT DEFAULT 0,
    `gender` INT DEFAULT 0,
    `name` VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    `username` VARCHAR(50),
    `psw` VARCHAR(50),
    `active` BOOL DEFAULT TRUE,
    `created_at` DATETIME DEFAULT CURRENT_DATE
  );

CREATE TABLE IF NOT EXISTS invoice(
id INT PRIMARY KEY AUTO_INCREMENT,
amount FLOAT DEFAULT 0,
tax FLOAT DEFAULT 0,
discount FLOAT DEFAULT 0,
total FLOAT DEFAULT 0,
employee INT,
employee_name VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
created_at DATETIME DEFAULT CURRENT_DATE,
FOREIGN KEY (employee) REFERENCES employee(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS invoice_drink(
invoice INT,
drink INT,
quantity INT,
drink_name VARCHAR(100),
FOREIGN KEY (invoice) REFERENCES invoice(id) ON DELETE SET NULL,
FOREIGN KEY (drink) REFERENCES drink(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS kpi(
year INT,
month INT,
value INT,
edit INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS other(
tax INT,
discount INT,
id INT KEY AUTO_INCREMENT
);

INSERT INTO other(tax, discount) VALUE (0,0);
INSERT INTO category (name) VALUES ('Trà sữa'),('Sinh tố'),('Cà phê'),('Khác');

INSERT INTO employee (id, position, gender, name, username, psw, active, created_at)
VALUES (1, 1, 0, 'hieu', 'admin', 'trunghieu7a1', 1, CURRENT_DATE);
```