-- SQLite
SELECT COUNT(*) FROM healthcare;

SELECT MAX(age), MIN(age) FROM healthcare;

SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;

SELECT COUNT(*) FROM healthcare WHERE 160 <= height and height <= 170; 

SELECT * FROM healthcare WHERE is_drinking = 1 AND waist != '' ORDER BY waist DESC LIMIT 5;

SELECT COUNT(*) FROM healthcare WHERE weight*10000 / (height*height) >= 30;

SELECT COUNT(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;

SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;

SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;

SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;

SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1 ;

SELECT id , weight*10000 / (height*height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;

SELECT COUNT(*) FROM healthcare WHERE waist >= 100 and blood_pressure >= 120;

SELECT id, age, height, weight FROM healthcare WHERE is_drinking = 1 ORDER BY smoking DESC LIMIT 10;

SELECT * FROM healthcare WHERE weight*10000 / (height*height) >= 30 AND iS_drinking = 1 ORDER BY weight DESC LIMIT 20;