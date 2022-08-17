-- SQLite
CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTERGER NOT NULL
);

.mode csv
.import users.csv users



SELECT * FROM users WHERE age >= 30;

SELECT first_name FROM users WHERE age >= 30 LIMIT 10:

SELECT age, last_name, first_name FROM users WHERE age >= 30 AND last_name = '김';

SELECT MIN(age), first_name FROM users WHERE last_name = '박';

SELECT MAX(balance), first_name FROM users;

SELECT count(*) FROM users WHERE phone LIKE '02-%';

SELECT count(*) FROM users WHERE first_name LIKE '%준';

SELECT count(*) FROM users WHERE phone LIKE '%-5114-%';

SELECT first_name FROM users ORDER BY age ASC LIMIT 10;

SELECT * FROM users ORDER BY age, last_name LIMIT 10;

SELECT first_name, last_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;