-- SQLite
SELECT COUNT(*) FROM healthcare;
SELECT COUNT(*) FROM healthcare WHERE age < 10;
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
SELECT COUNT(*) FROM healthcare WHERE va_left > 2.0 and va_right > 2.0;
SELECT DISTINCT sido FROM healthcare
SELECT COUNT(*) FROM healthcare WHERE gender = 2 and weight < 60;
