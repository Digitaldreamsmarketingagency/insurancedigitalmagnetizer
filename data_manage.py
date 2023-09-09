import sqlite3 as sql

t = """
    CREATE TABLE user(
        name,
        sub,
        img,
        link,
        id
    );"""

con =sql.connect("db.db")
con.execute("DELETE from user  WHERE id =2")
con.commit()
con.close()
