-- SQLite
CREATE TABLE classmates(
    name TXT,
    age INT,
    address TEXT
);

INSERT INTO classmates (name, age) VALUES ('이수영', 30)

SELECT * FROM classmates;
INSERT INTO classmates(name, age, address) VALUES ('김성태', 31, '부산');
INSERT INTO classmates VALUES ('노채리', 30, '부산');

SELECT rowid, * FROM classmates; 

