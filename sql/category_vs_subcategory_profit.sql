SELECT Category, [Sub-Category], ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category, [Sub-Category]
ORDER BY Total_Profit DESC;
