/*
1. Introducing Joins
*/
-- SELECT * FROM facts
-- INNER JOIN cities ON facts.id = cities.facts_id
-- LIMIT 10;

/*
2. Understanding Inner Joins
*/
-- SELECT c.*, f.name AS country_name
-- FROM facts AS f 
-- INNER JOIN cities AS c ON c.facts_id = f.id
-- LIMIT 5;

/*
3. Practicing Inner Joins
*/
-- SELECT f.name AS country, c.name AS capital_city FROM facts AS f 
-- INNER JOIN cities as c ON c.facts_id = f.id
-- WHERE c.capital = 1;

/*
4. Left Joins
*/
-- SELECT f.name AS country, f.population FROM facts as f
-- LEFT JOIN cities AS c on c.facts_id = f.id
-- WHERE c.name IS NULL;

/*
6.Finding the Most Populous Capital Cities
*/
-- SELECT c.name AS capital_city, f.name as country, c.population AS population 
-- FROM facts as f 
-- INNER JOIN cities AS c ON c.facts_id = f.id
-- WHERE c.capital = 1
-- ORDER BY 3 DESC
-- LIMIT 10;

/*
7. Combining Joins with Subqueries
*/
-- SELECT c.name AS capital_city, f.name AS country, c.population AS population
-- FROM facts AS f
-- INNER JOIN (SELECT * FROM cities WHERE capital = 1 AND population > 10000000) AS c ON c.facts_id = f.id
-- ORDER BY 3 DESC;

/*
8. Challenge: Complex Query with Joins and Subqueries
*/
SELECT f.name AS country, 
       c.urban_pop, 
       f.population AS total_pop, 
       (c.urban_pop / CAST(f.population AS FLOAT)) AS urban_pct
FROM facts as f 
INNER JOIN (
            SELECT facts_id,
                   SUM(population) AS urban_pop
            FROM cities
            GROUP BY 1
            ) AS c ON c.facts_id = f.id 
WHERE urban_pct > 0.5
ORDER BY 4 ASC;
