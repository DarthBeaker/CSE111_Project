from flask import Flask, render_template, request, jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
db = "sql/game_data.sqlite"

def get_conn(_db):
    conn = None
    try:
        conn = sqlite3.connect(_db)
    except Error as e:
        print(e)
    return conn

def close_conn(_conn):
    try:
        _conn.close()
    except Error as e:
        print(e)
    return



@app.route("/")
def index():
    conn = get_conn(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()
    cursor.execute('SELECT * FROM teams')
    teams = cursor.fetchall()
    cursor.execute('SELECT * FROM coaches')
    coaches = cursor.fetchall()
    close_conn(conn)
    return render_template("index.html",players=players,teams=teams,coaches=coaches)