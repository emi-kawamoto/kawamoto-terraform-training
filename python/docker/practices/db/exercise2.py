import sqlite3

db_name = "flinters_base"
con = sqlite3.connect(db_name)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products(id text,naddme text, price integer);")
cur.execute("INSERT INTO products VALUES('001', 'sample', 10000);")
cur.execute("SELECT * FROM products;")
for row in cur:
    print(row[0], row[1], row[2])
cur.execute("DROP TABLE products")
con.close()