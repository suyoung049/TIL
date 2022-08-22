-- SQLite

CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT
);

INSERT INTO users VALUES 
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 2);

CREATE TABLE role (
    id INT PRIMARY KEY, 
    title TEXT
);

INSERT INTO role VALUES 
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

CREATE TABLE articles (
    id INT PRIMARY KEY, 
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES 
    (1, '1번글', '111', 1),
    (2, '2번글', '222', 2),
    (3, '3번글', '333', 1),
    (4, '4번글', '444', NULL);


.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;

SELECT * FROM users JOIN role
ON users.role_id = role.id
WHERE role.title = 'staff';

SELECT * FROM users JOIN role
ON users.role_id = role.id
ORDER BY users.name DESC;

SELECT * FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id;
--  INNER JOIN 실행시 NULL 자료는 생략

SELECT * FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- 위의 INNERJOIN 결과와 동일

SELECT * FROM articles FULL OUTER JOIN users
ON users.id = articles.user_id;

SELECT * 
FROM users CROSS JOIN role;