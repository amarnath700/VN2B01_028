import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234",
                       database="family")
con.autocommit = True
cursor = con.cursor()

cursor.execute('''UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = 'M' ''')
cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())