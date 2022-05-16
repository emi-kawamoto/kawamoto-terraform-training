import MySQLdb
import os

conn = MySQLdb.connect(
    user=os.environ['MySQL_LOCAL_USER'],
    passwd=os.environ['MySQL_LOCAL_PASS'],
    host='localhost',
    db='exercise')

cur = conn.cursor()

sql = "SELECT * FROM employees"
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
  print(row)

cur.close()
conn.close()
