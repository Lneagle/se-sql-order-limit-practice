import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')

products = pd.read_sql("""
SELECT *
 FROM products;
""", conn)
print(products)

step_1 = pd.read_sql("""
SELECT *
    FROM products
    ORDER BY productCode DESC;
""", conn)
print(step_1)

step_2 = pd.read_sql("""
SELECT productCode, productName, productLine, productVendor
    FROM products
    ORDER BY productLine, productName;
""", conn)
print(step_2)

step_3 = pd.read_sql("""
SELECT COUNT(DISTINCT productLine)
    FROM products
""", conn)
print(step_3)

step_4 = pd.read_sql("""
SELECT productName, quantityInStock, MSRP, buyPrice, MSRP - buyPrice AS difference
    FROM products
    ORDER BY difference DESC, CAST(quantityInStock AS INTEGER) ASC;
""", conn)
print(step_4)

step_5 = pd.read_sql("""
SELECT productName, productLine, MSRP, buyPrice, abs(buyPrice - MSRP) AS abs_difference
    FROM products
    WHERE productLine = "Classic Cars"
    ORDER BY abs_difference DESC
    LIMIT 10;
""", conn)
print(step_5)

conn.close()