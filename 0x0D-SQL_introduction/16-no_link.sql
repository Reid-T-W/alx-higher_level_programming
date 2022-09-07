-- lists all non-null records of a table in desending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
