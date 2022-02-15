import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234")
con.autocommit = True
cursor = con.cursor()
s = '''CREATE DATABASE family'''
cursor.execute(s)
print("Database is Successfully Created")
