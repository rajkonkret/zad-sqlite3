import sqlite3

sql_conn = sqlite3.connect('sqllite_python.db')
cursor = sql_conn.cursor()
query = '''
CREATE TABLE developers (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
emai TEXT NOT NULL UNIQUE,
joining_date DATETIME,
salary REAL NOT NULL);
'''
insert = '''
INSERT INTO developers (ID,NAME,EMAI,SALARY) VALUES(1,"radek","RAJ@WP.PL", 1000);'''
cursor.execute(insert)
sql_conn.commit()
sql_conn.close()