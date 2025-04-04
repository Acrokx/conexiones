import psycopg2

conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="12345", host="localhost"
)


cursor = conn.cursor()
cursor.execute('SELECT * FROM tabla')

for row in cursor.fetchall():
    print(row)

conn.close()
