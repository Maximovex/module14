import sqlite3
import random
connection=sqlite3.connect('not_telegram.db')
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 age INTEGER,
 balance INTEGER NOT NULL
 )''')
for i in range(1,11):
    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",
                   (f'User{i}',f'example{i}@gmail.com',i*10,1000)
                   )

cursor.execute("SELECT id FROM Users")
num_users=len(cursor.fetchall())

for i in range(num_users//2):
    cursor.execute("UPDATE Users SET balance=? WHERE id=?",(500,i*2+1,))

for i in range(num_users//3):
    cursor.execute("DELETE FROM Users WHERE id=?",(i*3+1,))

cursor.execute("SELECT * FROM Users WHERE age != 60")
users=cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')




connection.commit()
connection.close()
