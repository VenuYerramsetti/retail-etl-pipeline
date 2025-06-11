SELECT [Product Name], SUM(Sales) AS Sales
FROM superstore
GROUP BY [Product Name]
ORDER BY Sales DESC
LIMIT 10;
