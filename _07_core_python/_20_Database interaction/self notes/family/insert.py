import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234",
                       database="family")
con.autocommit = True
cursor = con.cursor()

cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX) VALUES ('Ramya', 'Rama priya', 27, 'F'
)''')

insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX)   VALUES (%s, %s, %s, %s)"

data = [('Krishna', 'Sharma', 19, 'M'),
   ('Raj', 'Kandukuri', 20, 'M'),
   ('Ramya', 'Ramapriya', 25, 'M'),
   ('Mac', 'Mohan', 26, 'M')]
cursor.executemany(insert_stmt, data)
print("inserted Successfully")