-- 8-cities_of_california_subquery.sql
-- Lists all cities in California (id and name only) without using JOIN

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;

