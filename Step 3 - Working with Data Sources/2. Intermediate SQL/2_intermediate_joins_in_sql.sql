/*
2.Joining Three Tables
*/
-- SELECT t.track_id, 
--     t.name AS track_name, 
--     m.name as track_type, 
--     il.unit_price,
--     il.quantity
-- FROM track AS t
-- INNER JOIN invoice_line AS il ON il.track_id = t.track_id
-- INNER JOIN media_type AS m ON m.media_type_id = t.media_type_id
-- WHERE il.invoice_id = 4;

-- -- other way is

-- SELECT
--     il.track_id,
--     t.name track_name,
--     mt.name track_type,
--     il.unit_price,
--     il.quantity
-- FROM invoice_line il
-- INNER JOIN track t ON t.track_id = il.track_id
-- INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
-- WHERE il.invoice_id = 4;

/*
3.Joining More Than Three Tables
*/
-- SELECT
--     il.track_id,
--     t.name AS track_name,
--     ar.name AS artist_name,
--     mt.name AS track_type,
--     il.unit_price,
--     il.quantity
-- FROM invoice_line il
-- INNER JOIN track AS t ON t.track_id = il.track_id
-- INNER JOIN media_type AS mt ON mt.media_type_id = t.media_type_id
-- INNER JOIN album AS al ON al.album_id = t.album_id
-- INNER JOIN artist AS ar ON ar.artist_id = al.artist_id
-- WHERE il.invoice_id = 4;

/*
4.Combining Multiple Joins with Subqueries
*/
-- SELECT ta.album_title AS album,
--        ta.artist_name AS artist,
--        COUNT(*) AS tracks_purchased
-- FROM invoice_line AS il
-- INNER JOIN (
--             SELECT t.track_id,
--                    al.title AS album_title,
--                    ar.name AS artist_name                   
--             FROM track AS t 
--             INNER JOIN album AS al ON al.album_id = t.album_id
--             INNER JOIN artist AS ar ON ar.artist_id = al.artist_id
--            ) AS ta 
--            ON ta.track_id = il.track_id
-- GROUP BY 1, 2
-- ORDER BY 3 DESC
-- LIMIT 5;

/*
5.Recursive Joins
*/
-- SELECT e1.first_name || " " || e1.last_name AS employee_name,
--        e1.title AS employee_title,
--        e2.first_name || " " || e2.last_name AS supervisor_name,
--        e2.title AS supervisor_title
-- FROM employee AS e1
-- LEFT JOIN employee AS e2 ON e2.employee_id = e1.reports_to
-- ORDER BY 1

/*
6.Pattern Matching Using Like
*/
-- SELECT first_name,
--        last_name,
--        phone
-- FROM customer
-- WHERE first_name LIKE "%Belle%"

/*
7.Generating Columns With The Case Statement
*/
SELECT c.first_name || " " || c.last_name AS customer_name,
       COUNT(i.invoice_id) AS number_of_purchases,
       SUM(i.total) AS total_spent,
       CASE
       WHEN SUM(i.total) < 40 THEN 'small spender'
       WHEN SUM(i.total) < 100 THEN 'regular'
       ELSE 'big spender'
       END
       AS customer_category
FROM invoice AS i 
INNER JOIN customer AS c ON c.customer_id = i.customer_id
GROUP BY 1
ORDER BY 1;



