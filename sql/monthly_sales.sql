SELECT 
    strftime('%Y-%m', [Order Date]) AS Month,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;
