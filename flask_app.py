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

#route for hoempage
@app.route('/index.html')
def index_():
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


#route for Q1
@app.route('/Q1.html')
def index_Q1():


    return render_template('Q1.html')

#route for Q2
@app.route('/Q2.html')
def index_Q2():


    return render_template('Q2.html')


#route for Q3
@app.route('/Q3.html')
def index_Q3():


    return render_template('Q3.html')

#route for Q4
@app.route('/Q4.html')
def index_Q4():


    return render_template('Q4.html')

#route for Q5
@app.route('/Q5.html')
def index_Q5():


    return render_template('Q5.html')

#route for Q6
@app.route('/Q6html')
def index_Q6():


    return render_template('Q6.html')


#route for Q7
@app.route('/Q7.html')
def index_Q7():


    return render_template('Q7.html')

#route for Q8
@app.route('/Q8.html')
def index_Q8():


    return render_template('Q8.html')

#route for Q9
@app.route('/Q9.html')
def index_Q9():


    return render_template('Q9.html')

#route for Q10
@app.route('/Q10.html')
def index_Q10():


    return render_template('Q10.html')

#route for Q11
@app.route('/Q11.html')
def index_Q11():


    return render_template('Q11.html')

#route for Q12
@app.route('/Q12.html')
def index_Q12():


    return render_template('Q12.html')

#route for Q13
@app.route('/Q13.html')
def index_Q13():


    return render_template('Q13.html')

#route for Q14
@app.route('/Q14.html')
def index_Q14():


    return render_template('Q14.html')

#route for Q15
@app.route('/Q15.html')
def index_Q15():


    return render_template('Q15.html')

#route for Q16
@app.route('/Q16.html')
def index_Q16():


    return render_template('Q16.html')

#route for Q3
@app.route('/Q17.html')
def index_Q17():


    return render_template('Q17.html')

#route for Q18
@app.route('/Q18.html')
def index_Q18():


    return render_template('Q18.html')


