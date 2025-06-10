#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
import pandas as pd

conn = sqlite3.connect("output/retail_data.db")

query = "SELECT * FROM superstore LIMIT 5;"
df = pd.read_sql(query, conn)

print(df)
conn.close()

