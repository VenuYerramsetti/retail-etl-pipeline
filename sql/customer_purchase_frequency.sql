SELECT [Customer Name], COUNT(DISTINCT [Order ID]) AS Orders, ROUND(SUM(Sales), 2) AS Sales
FROM superstore
GROUP BY [Customer Name]
ORDER BY Orders DESC
LIMIT 10;
