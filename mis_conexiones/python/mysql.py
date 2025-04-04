import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='tienda'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM tabla')

for row in cursor.fetchall():
    print(row)

conn.close()
