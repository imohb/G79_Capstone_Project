import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="IdlP#bxj59",
	)

my_cursor = mydb.cursor()
# uncomment to create new databases
# my_cursor.execute("CREATE DATABASE conversations")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)