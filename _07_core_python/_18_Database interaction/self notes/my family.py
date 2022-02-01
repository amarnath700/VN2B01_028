import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="amarnath7008@"
)

print(mydb)