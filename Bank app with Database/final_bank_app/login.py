
import mysql.connector as SQLC

def login(acc,pwd):
    db=SQLC.connect(host="localhost",user="root",password="root",database="BANK1")
    c=db.cursor()
    c.execute("SELECT 1 FROM ACCOUNTS WHERE ACCOUNT=%s AND PASSWORD=%s",(acc,pwd))
    return c.fetchone() is not None
