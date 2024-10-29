-- Script.
SELECT city,AVG(temprature) AS avg_temp 
GROUP BY city WHERE IN month(7,8)
ORDER BY temprature DESC
LIMIT 3;
