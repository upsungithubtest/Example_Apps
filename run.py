"""
CREATE TABLE `friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `LastName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`id`)
);

export FLASK_APP=run.py
flask run --host=0.0.0.0
python -m flask run
"""
import os
import ast
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        dbhost = os.getenv("DBHOST", "127.0.0.1")
        dbname = os.getenv("DBNAME", "friends")
        dbuser = os.getenv("BUSER", "devuser")
        dbpass = os.getenv("DBPASS", "devPW")

        self.con = pymysql.connect(host=dbhost, user=dbuser, password=dbpass, db=dbname, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT FirstName, LastName FROM friends LIMIT 50")
        result = self.cur.fetchall()

        return result

@app.route('/')
def friends():

    def db_query():
        db = Database()
        emps = db.list_employees()

        return emps

    res = db_query()

    return render_template('friends_list.html', result=res)



