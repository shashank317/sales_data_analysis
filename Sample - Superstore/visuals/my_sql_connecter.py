import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",              # ✅ your MySQL Workbench username
    password="root",  # ✅ your password here
    database="salesdb"       # ✅ replace with your actual database name
)

# Run SQL Query
query = "SELECT * FROM sales_data"  # ✅ your table name
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Show top 5 rows
print(df.head())
