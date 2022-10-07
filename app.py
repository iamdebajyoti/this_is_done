
# A very simple Flask Hello World app for you to get started with...

import sqlite3
import random
import flask
from flask import Flask, session, render_template, request, g
import os

app = Flask(__name__)
app.secret_key = "nndwqwqjwqwqqjjej317317091uodqndnq"



@app.route('/')
def this_is_done():
    data = get_db()
    # return '<h1><b>Hello from Laxmi!!!!!</b></h1>'
    return str(data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("./db/this_is_done.db")
        cursor = db.cursor()
        cursor.execute("select * from ToDO_List")

    # return db
    return cursor.fetchall()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/ledger')
def hello_ledger():
    return 'Hello from Laxmi!'


if __name__ == '__main__':
    # app.run(host="localhost", port=5099, debug=True)
    app.run()
