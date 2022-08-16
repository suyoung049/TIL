-- SQLite
SELECT * FROM exaples;

CREATE TABLE classmates(
    id INTERGER PRIMARY KEY,
    name TEXT
);
SELECT * FROM exaples
-- 테이블 조회
.headers on

.mode colum 

.tables

.schema classmates

INSERT INTO classmates VALUES(1, '조세호');

SELECT * FROM classmates;

INSERT INTO classmates VALUES(2, '이수영');

DROP TABLE classmates;
