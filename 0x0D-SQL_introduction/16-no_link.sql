-- lists all non-null records of a table in desending score
SELECT * FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
