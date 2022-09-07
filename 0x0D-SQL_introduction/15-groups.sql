-- count the number of distinct scores
SELECT score, COUNT(DISTINCT(score)) as number
FROM second_table
