import sqlite3

connection=sqlite3.connect('not_telegram.db')
cursor=connection.cursor()

cursor.execute("DELETE FROM Users WHERE id=?",(6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users=cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance=cursor.fetchone()[0]
print(sum_balance/total_users)

connection.commit()
connection.close()
