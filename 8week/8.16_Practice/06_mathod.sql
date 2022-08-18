-- SQLite
SELECT * FROM users LIMIT 5;

SELECT last_name || first_name AS 이름,
    age,
    country,
    phone,
    balance
FROM users LIMIT 5;

SELECT LENGTH(country), country FROM users LIMIT 6;

SELECT first_name, phone, REPLACE(phone, '-', '')
FROM users LIMIT 5;

SELECT MOD(5, 2) FROM users LIMIT 1;

SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14) FROM users LIMIT 1;

SELECT last_name ,COUNT(*) FROM users GROUP BY last_name;

SELECT last_name ,COUNT(last_name) FROM users GROUP BY last_name 
HAVING COUNT(last_name) > 100 ;

