import csv

import pymysql
import config



cnx = pymysql.connect(host=config.dbhost, user=config.dbuser,
password=config.dbpass, db='',
cursorclass=pymysql.cursors.DictCursor)

cur = cnx.cursor()

# cur.execute("SELECT FirstName, LastName FROM friends LIMIT 50")
sql = f"CREATE DATABASE IF NOT EXISTS {config.dbname}"
print(sql)
cur.execute(sql)

sql = f"""CREATE TABLE IF NOT EXISTS {config.dbname}.friends (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `LastName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`id`)
)"""
cur.execute(sql)


sql = f"TRUNCATE {config.dbname}.friends"
cur.execute(sql)

csvfile = 'database/friends.csv'

rows = csv.reader(open(csvfile))

for row in rows:
    print(row[0],row[1])
    sql = f"INSERT INTO {config.dbname}.friends (FirstName,LastName) VALUES (%s,%s)"
    cur.execute(sql,(row[0],row[1]))
    # print(sql)

cnx.commit()
