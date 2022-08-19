-- SQLite
select * FROM albums ORDER BY Title
LIMIT 20;

SELECT COUNT(*) AS "고객 수" FROM customers;

SELECT FirstName '이름', LastName '성' FROM customers 
WHERE Country = 'USA' ORDER BY "이름" DESC LIMIT 5;

SELECT COUNT(*) AS '송장수' FROM invoices 
WHERE BillingPostalCode  NOT NULL;

SELECT * FROM invoices 
WHERE BillingPostalCode IS NULL ORDER BY InvoiceDate DESC LIMIT 5;

SELECT STRFTIME("%Y",InvoiceDate) FROM invoices;

SELECT COUNT(*) FROM invoices
WHERE STRFTIME("%Y",InvoiceDate) = '2013';

SELECT CustomerId 고객ID, FirstName 이름, LastName 성 
FROM customers
WHERE FirstName LIKE 'L%' ORDER BY 고객ID;

SELECT COUNT(*) "고객 수" , country "나라" 
FROM customers GROUP BY country ORDER BY "고객 수" DESC
LIMIT 5;

SELECT ArtistId, count(*) "앨범 수" FROM albums 
GROUP BY ArtistId ORDER BY "앨범 수" DESC LIMIT 1;

SELECT ArtistId, count(*) "앨범 수" FROM albums 
GROUP BY ArtistId HAVING "앨범 수" >= 10 ORDER BY "앨범 수" DESC;

SELECT COUNT(*) "고객 수", Country, State FROM customers
WHERE State NOT NULL 
GROUP BY Country, State ORDER BY "고객 수" DESC, Country DESC
LIMIT 5;

SELECT CustomerId 고객ID, 
CASE 
     WHEN Fax IS NULL THEN "X"
     WHEN Fax NOT NULL THEN "O"

END AS "Fax 유/무"
FROM customers LIMIT 5;



SELECT LastName, FirstName, 
(CAST(STRFTIME("%Y", 'now') AS INT) - CAST(STRFTIME("%Y",BirthDate) AS INT) + 1 ) AS 나이
FROM employees ORDER BY EmployeeId;

SELECT ArtistId FROM albums 
GROUP BY ArtistId ORDER BY COUNT(*) DESC LIMIT 1;

SELECT Name FROM artists
WHERE ArtistId = (SELECT ArtistId FROM albums 
GROUP BY ArtistId ORDER BY COUNT(*) DESC LIMIT 1);

SELECT GenreId, COUNT(*) FROM tracks 
GROUP BY GenreId ORDER BY COUNT(*) LIMIT 1;

SELECT Name FROM genres
WHERE GenreId = (SELECT GenreId FROM tracks 
GROUP BY GenreId ORDER BY COUNT(*) LIMIT 1);