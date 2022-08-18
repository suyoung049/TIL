-- SQLite
SELECT smoking, COUNT(smoking) FROM healthcare WHERE smoking != '' GROUP BY smoking;

SELECT is_drinking, COUNT(is_drinking) FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;

SELECT is_drinking, COUNT(is_drinking) FROM healthcare WHERE blood_pressure >=200 GROUP BY is_drinking;

SELECT sido, COUNT(sido) FROM healthcare GROUP BY sido HAVING COUNT(sido) >= 50000;

SELECT height, COUNT(height) FROM healthcare GROUP BY height ORDER BY COUNT(height) DESC LIMIT 5;

SELECT height, weight, COUNT(*) FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;

SELECT is_drinking, AVG(waist), COUNT(is_drinking) FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;

SELECT gender, ROUND(AVG(va_left),2) "평균 왼쪽 시력", 
ROUND(AVG(va_right),2) "평균 오른쪽 시력" FROM healthcare GROUP BY gender;

SELECT age, ROUND(AVG(height),2) "평균 키", 
ROUND(AVG(weight),2) "평균 몸무게" FROM healthcare 
GROUP BY age HAVING "평균 키" >= 160 AND "평균 몸무게" >= 60;

SELECT is_drinking, smoking, ROUND(AVG(weight*10000 / (height*height)),2) AS "평균 BMI"
FROM healthcare WHERE smoking != '' AND is_drinking != '' 
GROUP BY is_drinking, smoking;