import csv

import pymysql
import config

class Database:
    def __init__(self):

        self.con = pymysql.connect(host=config.dbhost, user=config.dbuser,
        password=config.dbpass, db=config.dbname,
        cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT FirstName, LastName FROM friends LIMIT 50")
        result = self.cur.fetchall()

        return result

csvfile = 'database/friends.csv'

rows = csv.reader(open(csvfile))

for row in rows:
    print(row[0],row[1])
