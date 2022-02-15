import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234",
                       database="family")
con.autocommit = True
cursor = con.cursor()

cursor.execute("SELECT * from EMPLOYEE WHERE AGE <23")
print(cursor.fetchall())