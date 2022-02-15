import psycopg2

con = psycopg2.connect(host="localhost",
                       user="postgres",
                       password="1234",
                       database="family")
con.autocommit = True
cursor = con.cursor()

cursor.execute("SELECT * from EMPLOYEE")
records = cursor.fetchall()
print("Total rows are:  ", len(records))
for row in records:
    print("first name: ", row[0])
    print("last name: ", row[1])
    print("age: ", row[2])
    print("Sex: ", row[3])
    print("\n")