-- Script.
SELECT city,AVG(value) AS avg_temp FROM tempratures
GROUP BY city WHERE IN month(7,8)
ORDER BY temprature DESC
LIMIT 3;
