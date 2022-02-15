import psycopg2

conn = psycopg2.connect(
    database="mydb",
    host="localhost",
    user="postgres",
    password="1234")

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Populating the table
insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)   VALUES (%s, %s, %s, %s, %s)"
data = [('Krishna', 'Sharma', 19, 'M', 2000),
   ('Raj', 'Kandukuri', 20, 'M', 7000),
   ('Ramya', 'Ramapriya', 25, 'M', 5000),
   ('Mac', 'Mohan', 26, 'M', 2000)]
cursor.executemany(insert_stmt, data)

#Retrieving specific records using the where clause
cursor.execute("SELECT * from EMPLOYEE WHERE AGE <23")
print(cursor.fetchall())

conn.commit()
# Closing the connection
conn.close()