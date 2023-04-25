import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()


# Создаем таблицу для хранения логинов и имен пользователей
cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY, 
                login TEXT NOT NULL, 
                name TEXT NOT NULL)""")
conn.commit()


