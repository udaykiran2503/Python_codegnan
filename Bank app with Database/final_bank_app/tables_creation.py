
import mysql.connector as SQLC

db=SQLC.connect(host="localhost",user="root",password="root",database="BANK1")
cur=db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ACCOUNTS(
ACCOUNT BIGINT NOT NULL,
PASSWORD VARCHAR(25) NOT NULL,
PRIMARY KEY(ACCOUNT)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
USERNAME VARCHAR(25) NOT NULL,
EMAIL VARCHAR(50) NOT NULL,
AMOUNT FLOAT NOT NULL,
ACCOUNT BIGINT NOT NULL,
FOREIGN KEY(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS TRANSACTIONS(
transaction_type VARCHAR(25) NOT NULL,
amount FLOAT NOT NULL,
ACCOUNT BIGINT NOT NULL,
foreign key(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)
);""")

db.commit()
print("Tables created.")

accounts_table_query = "INSERT IGNORE INTO ACCOUNTS (ACCOUNT, PASSWORD) VALUES (%s, %s)"

# single
cur.execute(accounts_table_query, (123, "abc"))

# multiple
multiple_accounts = [(456, "def"), (789, "ghi"), (111, "jkl"), (222, "mno")]
cur.executemany(accounts_table_query, multiple_accounts)

db.commit()

cur.executemany(accounts_table_query, multiple_accounts)

print("Inserted records into ACCOUNTS table")


# Insert into USERS

users_table_query = """INSERT INTO USERS (USERNAME, EMAIL, AMOUNT, ACCOUNT) 
                       VALUES(%s, %s, %s, %s)"""

# Single user record
single_user = ("Pavan", "21jr1a44c1@gmail.com", 1900.0, 123)
cur.execute(users_table_query, single_user)

# Multiple user records
multiple_users = [
    ("Ravi", "ravi@gmail.com", 5000.0, 456),
    ("Teja", "teja@gmail.com", 6000.0, 789),
    ("Manu", "manu@gmail.com", 2000.0, 111),
    ("Hari", "hari@gmail.com", 3500.0, 222),
]
cur.executemany(users_table_query, multiple_users)

print("Inserted records into USERS table")

# Insert sample TRANSACTIONS (Optional)

transactions_table_query = """INSERT INTO TRANSACTIONS (transaction_type, amount, ACCOUNT) 
                              VALUES(%s, %s, %s)"""

sample_transactions = [
    ("DEPOSIT", 500, 123),
    ("WITHDRAW", 200, 123),
    ("DEPOSIT", 700, 456),
    ("TRANSFER_SENT", 300, 456),
    ("TRANSFER_RECEIVED", 300, 789)
]

cur.executemany(transactions_table_query, sample_transactions)

print("Inserted records into TRANSACTIONS table")

db.commit()
#db.close()

print("All  data inserted successfully!")
