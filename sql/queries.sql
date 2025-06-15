-- sql/top_10_products.sql
-- 🔝 Top 10 Selling Products by Sales
SELECT [Product Name], SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;

-- sql/total_sales_by_region.sql
-- 🌍 Total Sales per Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- sql/profit_by_category.sql
-- 💰 Profit by Category
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

-- sql/monthly_sales.sql
-- 📆 Monthly Sales
SELECT strftime('%Y-%m', [Order Date]) AS Month,
       ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- sql/customer_purchase_frequency.sql
-- 👤 Customer Purchase Frequency
SELECT [Customer Name], COUNT(*) AS Purchase_Count
FROM superstore
GROUP BY [Customer Name]
ORDER BY Purchase_Count DESC;

-- sql/cumulative_sales_by_month.sql
-- 📈 Cumulative Monthly Sales (requires SQLite 3.25+)
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
    ROUND(SUM(Monthly_Sales) OVER (ORDER BY Month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS Cumulative_Sales
FROM monthly_sales;
