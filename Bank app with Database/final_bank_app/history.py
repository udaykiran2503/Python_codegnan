
import mysql.connector as SQLC

def mini_statement(acc):
    db=SQLC.connect(host="localhost",user="root",password="root",database="BANK1")
    c=db.cursor()
    c.execute("SELECT transaction_type,amount FROM TRANSACTIONS WHERE ACCOUNT=%s ORDER BY ROWID DESC LIMIT 5",(acc,))
    rows=c.fetchall()
    if not rows: return "No transactions."
    out="---- Mini Statement ----\n"
    for r in rows:
        out+=f"Type: {r[0]}, Amount: {r[1]}\n"
    return out
