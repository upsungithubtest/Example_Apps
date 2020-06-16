"""
CREATE TABLE `friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `LastName` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`id`)
);

export FLASK_APP=run.py
flask run --host=0.0.0.0
python -m flask run --host=0.0.0.0

export FLASK_APP=run.py ; python import_csv.py ; python -m flask run --host=0.0.0.0

gunicorn --bind 0.0.0.0:5000  --log-level=debug app:app
gunicorn --timeout 120 -w 4 --bind 0.0.0.0:80 -k gevent --log-level=debug app:app
"""

from flask import Flask, render_template
import pymysql
import config

app = Flask(__name__)


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

@app.route('/')
def friends():

    def db_query():
        db = Database()
        emps = db.list_employees()

        return emps

    res = db_query()

    return render_template('friends_list.html', result=res)

# run the app.
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


