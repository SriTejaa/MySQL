import mysql.connector

conn = mysql.connector.connect(
    host = '138.68.140.83',
    user = "sriteja",
    password = "Sriteja@123",
    database = "dbSriteja"
)

cursor = conn.cursor()

cursor.execute(" select * from item;")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
cursor.close()
conn.close()