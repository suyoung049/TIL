-- SQLite
SELECT * FROM playlist_track AS 'A' 
ORDER BY playlistId DESC LIMIT 5;

SELECT * FROM tracks AS 'B' 
ORDER BY TrackId LIMIT 5;

SELECT A.PlaylistId, B.Name FROM playlist_track AS 'A'
JOIN tracks AS 'B' ON A.TrackId = B.TrackId
ORDER BY A.playlistId DESC LIMIT 10;

SELECT A.PlaylistId, B.Name FROM playlist_track AS 'A'
JOIN tracks AS 'B' ON A.TrackId = B.TrackId
where A.playlistId = 10
ORDER BY B.Name DESC LIMIT 20;

SELECT COUNT(*) FROM tracks AS 'A' 
JOIN artists AS 'B' ON A.Composer = b.Name;

SELECT * FROM tracks AS 'A' 
JOIN artists AS 'B' ON A.Composer = b.Name LIMIT 20;

SELECT COUNT(*) FROM tracks AS 'A' 
LEFT OUTER JOIN artists AS 'B' ON A.Composer = b.Name;

SELECT InvoiceLineId, InvoiceId FROM invoice_items
ORDER BY InvoiceId LIMIT 5;

SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId LIMIT 5;

SELECT B.InvoiceId, A.InvoiceLineId FROM invoice_items AS 'A'
JOIN invoices AS 'B' ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC LIMIT 5;

SELECT InvoiceId, InvoiceLineId FROM invoice_items
ORDER BY InvoiceId DESC LIMIT 5;

SELECT A.InvoiceId, B.CustomerId FROM invoices AS 'A'
JOIN customers AS 'B' ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId DESC LIMIT 5;

SELECT B.InvoiceId, A.InvoiceLineId, C.CustomerId FROM invoice_items AS 'A'
JOIN invoices AS 'B' ON A.InvoiceId = B.InvoiceId 
JOIN Customers AS 'C' ON B.CustomerId = C.CustomerId
GROUP BY B.InvoiceId
ORDER BY B.InvoiceId DESC LIMIT 5;

SELECT B.InvoiceId, A.InvoiceLineId, C.CustomerId FROM invoice_items AS 'A'
JOIN invoices AS 'B' ON A.InvoiceId = B.InvoiceId 
JOIN Customers AS 'C' ON B.CustomerId = C.CustomerId
ORDER BY B.InvoiceId DESC LIMIT 30;

SELECT C.CustomerId, COUNT(*) FROM invoice_items AS 'A'
JOIN invoices AS 'B' ON A.InvoiceId = B.InvoiceId 
JOIN Customers AS 'C' ON B.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId LIMIT 5;


SELECT CustomerId, COUNT(*) FROM customers
GROUP BY CustomerId LIMIT 20;

SELECT InvoiceId, COUNT(*) FROM Invoice_items
GROUP BY InvoiceId LIMIT 10 ;