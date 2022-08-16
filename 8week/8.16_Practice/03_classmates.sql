-- SQLite
sqlite3 tutorial.sqlite3
CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates values
('이수영', 30, '경기'),
('이호영', 26, '인천'),
('김성태', 31, '부산'),
('손흥민', 32, '런던'),
('박민규', 30, '성남');

SELECT rowid, * FROM classmates;

SELECT rowid, name FROM classmates LIMIT 2;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2; 

SELECT * FROM classmates WHERE address = '런던';

SELECT name FROM classmates WHERE age >= 30;

SELECT DISTINCT age FROM classmates;

SELECT DISTINCT address FROM classmates;

DELETE FROM classmates WHERE rowid = 1;

UPDATE classmates SET name = '김종민', address = '제주도' WHERE rowid = 4;

UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5

DROP TABLE classmates;