"""python training db2"""
import sqlite3

con = sqlite3.connect("flinters_base")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS \
            products( \
                id text, \
                name text, \
                price integer\
            );")
cur.execute("INSERT INTO products VALUES('001', 'sample', 10000)")

cur.execute("SELECT * FROM products")
for row in cur:
    print("レコードの値を表示：\n", row[0], row[1], row[2])

cur.execute("PRAGMA table_info('products');")
print("カラムの情報を表示：")
for row in cur:
    print(row[0], row[1], row[2])

con.close()
