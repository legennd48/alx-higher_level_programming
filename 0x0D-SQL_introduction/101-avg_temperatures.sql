-- Import in hbtn_0c_0 database this table temperatures.sql
-- using: mysql -u user_name -p hbtn_0c_0 < temperatures.sql
--  displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
