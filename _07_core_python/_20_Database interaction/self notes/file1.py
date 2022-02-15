import psycopg2

conn = psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="1234")

conn.autocommit =True

cursor = conn.cursor()

cursor.execute()