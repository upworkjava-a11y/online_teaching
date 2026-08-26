"""Official LeetCode Easy sample schemas/seeds for SQL sandbox (coexist with bank tables)."""

LEETCODE_SCHEMA_SQL = """
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS World;
DROP TABLE IF EXISTS Tweets;
DROP TABLE IF EXISTS Views;
DROP TABLE IF EXISTS cinema;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Followers;
DROP TABLE IF EXISTS EmployeeAttendance;
DROP TABLE IF EXISTS Teacher;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS ActorDirector;
DROP TABLE IF EXISTS MyNumbers;
DROP TABLE IF EXISTS EmployeeUNI;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Bonus;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Triangle;
DROP TABLE IF EXISTS Activity;
DROP TABLE IF EXISTS DailySales;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS Seat;
DROP TABLE IF EXISTS Scores;
DROP TABLE IF EXISTS LCCustomers;
DROP TABLE IF EXISTS LCOrders;

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    low_fats TEXT NOT NULL,
    recyclable TEXT NOT NULL
);

CREATE TABLE World (
    name TEXT PRIMARY KEY,
    continent TEXT,
    area INTEGER,
    population INTEGER,
    gdp INTEGER
);

CREATE TABLE Tweets (
    tweet_id INTEGER PRIMARY KEY,
    content TEXT NOT NULL
);

CREATE TABLE Views (
    article_id INTEGER,
    author_id INTEGER,
    viewer_id INTEGER,
    view_date DATE
);

CREATE TABLE cinema (
    id INTEGER PRIMARY KEY,
    movie TEXT,
    description TEXT,
    rating REAL
);

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    conditions TEXT
);

CREATE TABLE Followers (
    user_id INTEGER,
    follower_id INTEGER,
    PRIMARY KEY (user_id, follower_id)
);

CREATE TABLE EmployeeAttendance (
    emp_id INTEGER,
    event_day DATE,
    in_time INTEGER,
    out_time INTEGER
);

CREATE TABLE Teacher (
    teacher_id INTEGER,
    subject_id INTEGER,
    dept_id INTEGER
);

CREATE TABLE Courses (
    student TEXT,
    class TEXT,
    PRIMARY KEY (student, class)
);

CREATE TABLE ActorDirector (
    actor_id INTEGER,
    director_id INTEGER,
    timestamp INTEGER,
    PRIMARY KEY (actor_id, director_id, timestamp)
);

CREATE TABLE MyNumbers (
    num INTEGER
);

CREATE TABLE Employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE EmployeeUNI (
    id INTEGER,
    unique_id INTEGER,
    PRIMARY KEY (id, unique_id)
);

CREATE TABLE Employee (
    empId INTEGER PRIMARY KEY,
    name TEXT,
    supervisor INTEGER,
    salary INTEGER
);

CREATE TABLE Bonus (
    empId INTEGER PRIMARY KEY,
    bonus INTEGER
);

CREATE TABLE Product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT
);

CREATE TABLE Sales (
    sale_id INTEGER,
    product_id INTEGER,
    year INTEGER,
    quantity INTEGER,
    price INTEGER,
    PRIMARY KEY (sale_id, year)
);

CREATE TABLE Triangle (
    x INTEGER,
    y INTEGER,
    z INTEGER,
    PRIMARY KEY (x, y, z)
);

CREATE TABLE Activity (
    user_id INTEGER,
    session_id INTEGER,
    activity_date DATE,
    activity_type TEXT
);

CREATE TABLE DailySales (
    date_id DATE,
    make_name TEXT,
    lead_id INTEGER,
    partner_id INTEGER
);

CREATE TABLE Person (
    personId INTEGER PRIMARY KEY,
    lastName TEXT,
    firstName TEXT
);

CREATE TABLE Address (
    addressId INTEGER PRIMARY KEY,
    personId INTEGER,
    city TEXT,
    state TEXT
);

CREATE TABLE Seat (
    id INTEGER PRIMARY KEY,
    student TEXT
);

CREATE TABLE Scores (
    id INTEGER PRIMARY KEY,
    score REAL NOT NULL
);

CREATE TABLE LCCustomers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE LCOrders (
    id INTEGER PRIMARY KEY,
    customerId INTEGER NOT NULL
);
"""

LEETCODE_SEED_SQL = """
DELETE FROM Products;
DELETE FROM World;
DELETE FROM Tweets;
DELETE FROM Views;
DELETE FROM cinema;
DELETE FROM Patients;
DELETE FROM Followers;
DELETE FROM EmployeeAttendance;
DELETE FROM Teacher;
DELETE FROM Courses;
DELETE FROM ActorDirector;
DELETE FROM MyNumbers;
DELETE FROM EmployeeUNI;
DELETE FROM Employees;
DELETE FROM Bonus;
DELETE FROM Employee;
DELETE FROM Sales;
DELETE FROM Product;
DELETE FROM Triangle;
DELETE FROM Activity;
DELETE FROM DailySales;
DELETE FROM Address;
DELETE FROM Person;
DELETE FROM Seat;
DELETE FROM Scores;
DELETE FROM LCOrders;
DELETE FROM LCCustomers;

INSERT INTO Products (product_id, low_fats, recyclable) VALUES
(0, 'Y', 'N'), (1, 'Y', 'Y'), (2, 'N', 'Y'), (3, 'Y', 'Y'), (4, 'N', 'N');

INSERT INTO World (name, continent, area, population, gdp) VALUES
('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
('Albania', 'Europe', 28748, 2831741, 12960000000),
('Algeria', 'Africa', 2381741, 37100000, 188681000000),
('Andorra', 'Europe', 468, 78115, 3712000000),
('Angola', 'Africa', 1246700, 20609294, 100990000000);

INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'Vote for Biden'),
(2, 'Let us make America great again!');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
(1, 3, 5, '2019-08-01'), (1, 3, 6, '2019-08-02'), (2, 7, 7, '2019-08-01'),
(2, 7, 6, '2019-08-02'), (4, 7, 1, '2019-07-22'), (3, 4, 4, '2019-07-21'), (3, 4, 4, '2019-07-21');

INSERT INTO cinema (id, movie, description, rating) VALUES
(1, 'War', 'great 3D', 8.9), (2, 'Science', 'fiction', 8.5), (3, 'irish', 'boring', 6.2),
(4, 'Ice song', 'Fantacy', 8.6), (5, 'House card', 'Interesting', 9.1);

INSERT INTO Patients (patient_id, patient_name, conditions) VALUES
(1, 'Daniel', 'YFEV COUGH'), (2, 'Alice', ''), (3, 'Bob', 'DIAB100 MYOP'),
(4, 'George', 'ACNE DIAB100'), (5, 'Alain', 'DIAB201');

INSERT INTO Followers (user_id, follower_id) VALUES (0, 1), (1, 0), (2, 0), (2, 1);

INSERT INTO EmployeeAttendance (emp_id, event_day, in_time, out_time) VALUES
(1, '2020-11-28', 4, 32), (1, '2020-11-28', 55, 200), (1, '2020-12-03', 1, 42),
(2, '2020-11-28', 3, 33), (2, '2020-12-09', 47, 74);

INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES
(1, 2, 3), (1, 2, 4), (1, 3, 3), (2, 1, 1), (2, 2, 1), (2, 3, 1), (2, 4, 1);

INSERT INTO Courses (student, class) VALUES
('A', 'Math'), ('B', 'English'), ('C', 'Math'), ('D', 'Biology'),
('E', 'Math'), ('F', 'Computer'), ('G', 'Math'), ('H', 'Math'), ('I', 'Math');

INSERT INTO ActorDirector (actor_id, director_id, timestamp) VALUES
(1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 3), (1, 2, 4), (2, 1, 5), (2, 1, 6);

INSERT INTO MyNumbers (num) VALUES (8), (8), (3), (3), (1), (4), (5), (6);

INSERT INTO Employees (id, name) VALUES
(1, 'Alice'), (7, 'Bob'), (11, 'Meir'), (90, 'Winston'), (3, 'Jonathan');

INSERT INTO EmployeeUNI (id, unique_id) VALUES (3, 1), (11, 2), (90, 3);

INSERT INTO Employee (empId, name, supervisor, salary) VALUES
(3, 'Brad', NULL, 4000), (1, 'John', 3, 1000), (2, 'Dan', 3, 2000), (4, 'Thomas', 3, 4000);

INSERT INTO Bonus (empId, bonus) VALUES (2, 500), (4, 2000);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'Nokia'), (200, 'Apple'), (300, 'Siemens');

INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000), (2, 100, 2009, 12, 5000), (7, 200, 2011, 15, 9000);

INSERT INTO Triangle (x, y, z) VALUES (13, 15, 30), (10, 20, 15);

INSERT INTO Activity (user_id, session_id, activity_date, activity_type) VALUES
(1, 1, '2019-07-20', 'open_session'), (1, 1, '2019-07-20', 'scroll_down'),
(1, 1, '2019-07-20', 'end_session'), (2, 4, '2019-07-20', 'open_session'),
(2, 4, '2019-07-21', 'send_message'), (2, 4, '2019-07-21', 'end_session'),
(3, 2, '2019-07-21', 'open_session'), (3, 2, '2019-07-21', 'send_message'),
(3, 2, '2019-07-21', 'end_session'), (4, 3, '2019-06-25', 'open_session'),
(4, 3, '2019-06-25', 'end_session');

INSERT INTO DailySales (date_id, make_name, lead_id, partner_id) VALUES
('2020-12-8', 'toyota', 0, 1), ('2020-12-8', 'toyota', 1, 0),
('2020-12-8', 'toyota', 1, 2), ('2020-12-7', 'toyota', 0, 2),
('2020-12-7', 'toyota', 0, 1), ('2020-12-8', 'honda', 1, 2),
('2020-12-8', 'honda', 2, 1), ('2020-12-7', 'honda', 0, 1),
('2020-12-7', 'honda', 1, 2), ('2020-12-7', 'honda', 2, 1);

INSERT INTO Person (personId, lastName, firstName) VALUES
(1, 'Wang', 'Allen'), (2, 'Alice', 'Bob');

INSERT INTO Address (addressId, personId, city, state) VALUES
(1, 2, 'New York City', 'New York'), (2, 3, 'Leetcode', 'California');

INSERT INTO Seat (id, student) VALUES
(1, 'Abbot'), (2, 'Doris'), (3, 'Emerson'), (4, 'Green'), (5, 'Jeames');

INSERT INTO Scores (id, score) VALUES
(1, 3.50), (2, 3.65), (3, 4.00), (4, 3.85), (5, 4.00), (6, 3.65);

INSERT INTO LCCustomers (id, name) VALUES
(1, 'Joe'), (2, 'Henry'), (3, 'Sam'), (4, 'Max');

INSERT INTO LCOrders (id, customerId) VALUES
(1, 3), (2, 1);
"""

LEETCODE_PREVIEWS = {
    "Products": {"columns": ["product_id", "low_fats", "recyclable"], "rows": [[0, "Y", "N"], [1, "Y", "Y"], [3, "Y", "Y"]]},
    "World": {"columns": ["name", "continent", "area", "population", "gdp"], "rows": [["Afghanistan", "Asia", 652230, 25500100, 20343000000]]},
    "Views": {"columns": ["article_id", "author_id", "viewer_id", "view_date"], "rows": [[1, 3, 5, "2019-08-01"], [2, 7, 7, "2019-08-01"]]},
    "Tweets": {"columns": ["tweet_id", "content"], "rows": [[1, "Vote for Biden"], [2, "Let us make America great again!"]]},
    "cinema": {"columns": ["id", "movie", "description", "rating"], "rows": [[1, "War", "great 3D", 8.9], [5, "House card", "Interesting", 9.1]]},
    "Patients": {"columns": ["patient_id", "patient_name", "conditions"], "rows": [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]]},
    "Followers": {"columns": ["user_id", "follower_id"], "rows": [[0, 1], [2, 0], [2, 1]]},
    "EmployeeAttendance": {"columns": ["emp_id", "event_day", "in_time", "out_time"], "rows": [[1, "2020-11-28", 4, 32], [1, "2020-11-28", 55, 200]]},
    "Teacher": {"columns": ["teacher_id", "subject_id", "dept_id"], "rows": [[1, 2, 3], [2, 1, 1]]},
    "Courses": {"columns": ["student", "class"], "rows": [["A", "Math"], ["B", "English"], ["C", "Math"]]},
    "ActorDirector": {"columns": ["actor_id", "director_id", "timestamp"], "rows": [[1, 1, 0], [1, 1, 1], [1, 1, 2]]},
    "MyNumbers": {"columns": ["num"], "rows": [[8], [3], [1], [4]]},
    "Employees": {"columns": ["id", "name"], "rows": [[1, "Alice"], [7, "Bob"], [11, "Meir"]]},
    "EmployeeUNI": {"columns": ["id", "unique_id"], "rows": [[3, 1], [11, 2], [90, 3]]},
    "Employee": {"columns": ["empId", "name", "supervisor", "salary"], "rows": [[3, "Brad", None, 4000], [2, "Dan", 3, 2000]]},
    "Bonus": {"columns": ["empId", "bonus"], "rows": [[2, 500], [4, 2000]]},
    "Product": {"columns": ["product_id", "product_name"], "rows": [[100, "Nokia"], [200, "Apple"]]},
    "Sales": {"columns": ["sale_id", "product_id", "year", "quantity", "price"], "rows": [[1, 100, 2008, 10, 5000], [7, 200, 2011, 15, 9000]]},
    "Triangle": {"columns": ["x", "y", "z"], "rows": [[13, 15, 30], [10, 20, 15]]},
    "Activity": {"columns": ["user_id", "session_id", "activity_date", "activity_type"], "rows": [[1, 1, "2019-07-20", "open_session"], [2, 4, "2019-07-21", "end_session"]]},
    "DailySales": {"columns": ["date_id", "make_name", "lead_id", "partner_id"], "rows": [["2020-12-8", "toyota", 0, 1], ["2020-12-8", "honda", 1, 2]]},
    "Person": {"columns": ["personId", "lastName", "firstName"], "rows": [[1, "Wang", "Allen"], [2, "Alice", "Bob"]]},
    "Address": {"columns": ["addressId", "personId", "city", "state"], "rows": [[1, 2, "New York City", "New York"]]},
    "Seat": {"columns": ["id", "student"], "rows": [[1, "Abbot"], [2, "Doris"], [3, "Emerson"]]},
    "Scores": {"columns": ["id", "score"], "rows": [[1, 3.5], [2, 3.65], [3, 4.0]]},
    "LCCustomers": {"columns": ["id", "name"], "rows": [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]},
    "LCOrders": {"columns": ["id", "customerId"], "rows": [[1, 3], [2, 1]]},
}
