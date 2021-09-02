-- most sold tracks in the US

-- WITH track_sold_us AS(
--     SELECT il.track_id AS track_id, SUM(il.quantity) AS tracks_sold
--     FROM invoice_line AS il
--     INNER JOIN invoice AS i ON i.invoice_id = il.invoice_id
--     WHERE i.billing_country = 'USA'
--     GROUP BY 1
--     ORDER BY 2 DESC
--     ),
--     track_genre AS(
--     SELECT t.track_id AS track_id, g.name AS genre_name
--     FROM track AS t 
--     INNER JOIN genre AS g ON g.genre_id = t.genre_id
--     )

-- SELECT tg.genre_name AS genre_name, 
--        SUM(tsu.tracks_sold) AS total_track_sold,
--        ROUND(CAST(SUM(tsu.tracks_sold) AS FLOAT) / (SELECT SUM(tracks_sold) FROM track_sold_us) * 100, 2) AS percentage_sold
-- FROM track_genre AS tg 
-- INNER JOIN track_sold_us AS tsu ON tsu.track_id = tg.track_id
-- GROUP BY 1
-- ORDER BY 2 DESC;


-- WITH sales_employee_list AS(
--     SELECT * FROM employee WHERE title = "Sales Support Agent"
--     ),
--     sales_rep_sales AS(
--     SELECT c.support_rep_id AS sales_id, SUM(i.total) AS total_sales
--     FROM customer AS c 
--     INNER JOIN invoice AS i ON i.customer_id = c.customer_id
--     GROUP BY 1
--     )

-- SELECT sel.first_name || " " || sel.last_name AS sales_employee,
--        sel.hire_date,
--        srs.total_sales
-- FROM sales_employee_list AS sel 
-- INNER JOIN sales_rep_sales AS srs ON srs.sales_id = sel.employee_id
-- ORDER BY 3 DESC



-- --grouping total sales per country
-- SELECT billing_country, SUM(total) 
-- FROM invoice 
-- GROUP BY 1 
-- ORDER BY 2 DESC 

-- grouping total customesr per country
-- SELECT billing_country, COUNT(DISTINCT customer_id)
-- FROM invoice
-- GROUP BY 1
-- ORDER BY 2 DESC 


--countries_or_other

-- SELECT 
--     CASE
--         WHEN (
--             SELECT COUNT(*) FROM customer WHERE country = c.country 
--         ) = 1 THEN 'Other'
--         ELSE c.country
--         END AS country,
--         c.customer_id,
--         il.*
-- FROM invoice_line AS il 
-- INNER JOIN invoice AS i ON i.invoice_id = il.invoice_id
-- INNER JOIN customer AS c ON c.customer_id = i.customer_id

--total number of customers per country
-- SELECT country, COUNT(customer_id) FROM customer GROUP BY 1

--total value of sales per country
-- SELECT c.country, SUM(i.total)
-- FROM customer AS c 
-- INNER JOIN invoice AS i ON i.customer_id = c.customer_id
-- GROUP BY 1

-- average value sales per customer
----- total value sales / total number of custromers

--number of billings per country
-- SELECT billing_country, COUNT(invoice_id)
-- FROM invoice
-- GROUP BY billing_country
--------------------------------------------
WITH country_data AS(
        SELECT c.country AS country, 
               SUM(i.total) AS total_value, 
               COUNT(DISTINCT c.customer_id) AS total_customer
        FROM customer AS c 
        INNER JOIN invoice AS i ON i.customer_id = c.customer_id
        GROUP BY 1),

      billing_countries AS(
          SELECT billing_country, COUNT(invoice_id) AS total_invoice
          FROM invoice
          GROUP BY billing_country
      ),
      raw_data AS(
        SELECT 
            cd.country AS country,
            cd.total_customer AS customer,
            cd.total_value AS total,
            cd.total_value / cd.total_customer AS avg_cus,
            cd.total_value / bc.total_invoice AS avg_sales
        FROM country_data as cd 
        INNER JOIN billing_countries AS bc ON cd.country = bc.billing_country
        ORDER BY 3 DESC
      )

SELECT CASE
       WHEN rd.customer = 1 THEN "Other"
       ELSE rd.country
       END AS country,
       SUM(rd.customer),
       SUM(rd.total),
       SUM(rd.avg_cus),
       SUM(rd.avg_sales)
FROM raw_data as rd
GROUP BY 1




