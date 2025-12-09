
import mysql.connector as SQLC
from Single_email_send import singleEmailsender

def get_connection():
    return SQLC.connect(host="localhost",user="root",password="root",database="BANK1")

def get_user(account):
    db=get_connection(); cur=db.cursor()
    cur.execute("SELECT USERNAME,EMAIL,AMOUNT,ACCOUNT FROM USERS WHERE ACCOUNT=%s",(account,))
    r=cur.fetchone(); 
    db.close(); 
    return r

def update_balance(account,new):
    db=get_connection(); cur=db.cursor()
    cur.execute("UPDATE USERS SET AMOUNT=%s WHERE ACCOUNT=%s",(new,account))
    db.commit(); 
    db.close()

def log_transaction(account,typ,amt):
    db=get_connection(); cur=db.cursor()
    cur.execute("INSERT INTO TRANSACTIONS(transaction_type,amount,ACCOUNT) VALUES (%s,%s,%s)",(typ,amt,account))
    db.commit(); 
    db.close()
