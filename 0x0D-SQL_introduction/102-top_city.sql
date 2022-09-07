-- display the top three cities temperature during July and August ordered in desending order-- by temp

SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE (month >= 7 AND month <= 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
