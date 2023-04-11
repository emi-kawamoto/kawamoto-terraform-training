"""python training db1"""
import sqlite3

db_name = "test"
con = sqlite3.connect(db_name)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name text, age integer);")
cur.execute("INSERT INTO users VALUES('テスト たろう', 25)")
cur.execute("INSERT INTO users VALUES('テスト じろう', 20)")
cur.execute("SELECT * FROM users")
for row in cur:
    print(row[0], row[1])
cur.execute("DROP TABLE users")
con.close()
