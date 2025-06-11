WITH monthly_sales AS (
    SELECT 
        strftime('%Y-%m', [Order Date]) AS Month,
        ROUND(SUM(Sales), 2) AS Monthly_Sales
    FROM superstore
    GROUP BY Month
)
SELECT 
    Month,
    Monthly_Sales,
    ROUND(SUM(Monthly_Sales) OVER (ORDER BY Month), 2) AS Cumulative_Sales
FROM monthly_sales;
