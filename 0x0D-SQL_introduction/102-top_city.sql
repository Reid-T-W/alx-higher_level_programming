-- display the top three cities temperature during July and August ordered in desending order by temp

SELECT TOP 3 cities, AVG(value) as avg_temp
FROM temperature
WHERE month >= 7 and month <= 8
GROUP BY month
ORDER BY avg_temp DESC;


