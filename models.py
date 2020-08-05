import sqlite3 as sql
from os import path

ROOT = path.dirname(path.abspath((__file__)))

def create_posts(name, status):
    conn = sql.connect(path.join(ROOT, 'database.db'))
    curr = conn.cursor()
    curr.execute('insert into social (name, stat) values (?, ?)', (name,status))
    conn.commit()
    conn.close()

def see_posts():
    conn = sql.connect(path.join(ROOT, 'database.db'))
    curr = conn.cursor()
    curr.execute('select * from social')
    posts = curr.fetchall()
    return posts
