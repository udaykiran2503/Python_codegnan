
import mysql.connector as SQLC

db=SQLC.connect(host="localhost",
                user="root",
                password="root"
                )
cur=db.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS BANK1;")
print("Database BANK1 created.")
