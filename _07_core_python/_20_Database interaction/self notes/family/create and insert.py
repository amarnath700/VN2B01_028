import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234",
                       database="family")
con.autocommit = True
cursor = con.cursor()

cursor.execute('''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1)
)''')
print("table created Successfully")