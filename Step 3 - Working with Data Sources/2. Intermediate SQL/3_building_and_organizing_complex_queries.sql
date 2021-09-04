/*
3.The With Clause
*/
-- WITH playlist_info AS
--     (
--     SELECT pl.playlist_id AS playlist_id,
--            pl.name AS playlist_name,
--            t.name AS track_name,
--            (t.milliseconds / 1000) AS track_length
--     FROM playlist AS pl 
--     LEFT JOIN playlist_track AS pt ON pt.playlist_id = pl.playlist_id
--     LEFT JOIN track AS t ON t.track_id = pt.track_id
--     )

-- SELECT playlist_id,
--        playlist_name,
--        COUNT(track_name) AS number_of_tracks,
--        SUM(track_length) AS length_seconds
-- FROM playlist_info
-- GROUP BY 1, 2
-- ORDER BY 1;

/*
4.Creating Views
*/
-- CREATE VIEW customer_usa AS
--     SELECT * FROM customer
--     WHERE country = "USA";
-- DROP VIEW IF EXISTS customer_gt_90_dollars;
-- CREATE VIEW customer_gt_90_dollars AS
--     SELECT c.* FROM customer AS c 
--     INNER JOIN invoice AS i ON i.customer_id = c.customer_id
--     GROUP BY c.customer_id
--     HAVING SUM(i.total) > 90;
-- SELECT * FROM customer_gt_90_dollars;

/*
5.Combining Rows With Union
*/
-- SELECT * FROM customer_usa
-- UNION
-- SELECT* FROM customer_gt_90_dollars

/*
6.Combining Rows Using Intersect and Except
*/
-- Write a query that works out how many customers that are in the USA and have purchased more than $90 are assigned to each sales support agent.
-- WITH customer_usa_90 AS
--                     (
--                     SELECT * FROM customer_usa
--                     INTERSECT
--                     SELECT * FROM customer_gt_90_dollars
--                     )

-- SELECT e.first_name || " " || e.last_name AS employee_name,
--        COUNT(c.customer_id) AS customers_usa_gt_90
-- FROM employee AS e 
-- LEFT JOIN customer_usa_90 AS c ON e.employee_id = c.support_rep_id
-- WHERE e.title = 'Sales Support Agent'
-- GROUP BY 1
-- ORDER BY 1;

/*
7.Multiple Named Subqueries
*/
-- WITH 
--     customer_india AS
--                     (
--                     SELECT * FROM customer
--                     WHERE country = "India"
--                     ),
--     total_customer AS
--                     (
--                     SELECT customer_id, SUM(total) AS total FROM invoice
--                     GROUP BY 1
--                     )

-- SELECT c.first_name || " " || c.last_name AS customer_name,
--        tc.total AS total_purchases
-- FROM customer_india AS c 
-- INNER JOIN total_customer AS tc ON tc.customer_id = c.customer_id
-- ORDER BY 1;

/*
8.Challenge: Each Country's Best Customer
*/
-- writing a query to find the customer from each country that has spent the most money at our store.

-- WITH 
--     customer_purchase_country AS
--             (
--             SELECT c.customer_id, c.country, sum(i.total) AS total_purchases
--             FROM customer AS c 
--             INNER JOIN invoice AS i ON i.customer_id = c.customer_id
--             GROUP BY 1
--             )

-- SELECT cpc.country AS country, 
--        c.first_name || " " || c.last_name AS customer_name,
--        MAX(cpc.total_purchases) AS total_purchased
-- FROM customer_purchase_country AS cpc 
-- INNER JOIN customer AS c ON c.customer_id = cpc.customer_id
-- GROUP BY 1
-- ORDER BY 1;

----------------other way
WITH
    customer_country_purchases AS
        (
         SELECT
             i.customer_id,
             c.country,
             SUM(i.total) total_purchases
         FROM invoice i
         INNER JOIN customer c ON i.customer_id = c.customer_id
         GROUP BY 1, 2
        ),
    country_max_purchase AS
        (
         SELECT
             country,
             MAX(total_purchases) max_purchase
         FROM customer_country_purchases
         GROUP BY 1
        ),
    country_best_customer AS
        (
         SELECT
            cmp.country,
            cmp.max_purchase,
            (
             SELECT ccp.customer_id
             FROM customer_country_purchases ccp
             WHERE ccp.country = cmp.country AND cmp.max_purchase = ccp.total_purchases
            ) customer_id
         FROM country_max_purchase cmp
        )

SELECT
    cbc.country country,
    c.first_name || " " || c.last_name customer_name,
    cbc.max_purchase total_purchased
FROM customer c
INNER JOIN country_best_customer cbc ON cbc.customer_id = c.customer_id
ORDER BY 1 ASC



