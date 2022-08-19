-- SQLite
SELECT
    id,
    CASE
        WHEN gender = 1 THEN "남자"
        WHEN gender = 2 THEN "여자"

    END AS "성별"
FROM healthcare
LIMIT 5;

SELECT DISTINCT smoking 
FROM healthcare;

SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN "비흡연자"
        WHEN smoking = 2 THEN "흡연자"
        WHEN smoking = 3 THEN "꼴초"
        ELSE "무응답"

    END
FROM healthcare
LIMIT 10;



SELECT
    first_name,
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN "청소년"
        WHEN age <= 40 THEN "청년"
        WHEN age <= 90 THEN "중장년"
        ELSE "노년"

    END
FROM users
LIMIT 50;

SELECT COUNT(*) FROM users WHERE age = (SELECT MIN(age) FROM users);

SELECT
    COUNT(balance)
    FROM users
    WHERE balance > (SELECT AVG(balance) FROM users);

SELECT *
    FROM users
    WHERE (last_name = '유' AND first_name = '은정');

SELECT 
    COUNT(*)
    FROM users
    WHERE country = (SELECT 
    country
    FROM users
    WHERE first_name = '은정' AND last_name = '유');

SELECT 
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉,
    (SELECT AVG(age) FROM users) AS 평균나이
;


SELECT last_name, MIN(age) FROM users group by last_name;

SELECT last_name, first_name, age
FROM users WHERE (last_name, age) in (SELECT DISTINCT last_name, MIN(age) FROM users group by last_name) ORDER BY last_name;

