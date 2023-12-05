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


def execute_query_from_file(file_path, cursor):
    with open(file_path, 'r') as file:
        sql_query = file.read()
        cursor.execute(sql_query)

@app.route('/Q_insert.html')
def Q_insert():
    return render_template('Q_insert.html')

@app.route('/delete_from_players', methods=['POST'])
def delete_from_players(): 
    sql1 = '''
        DELETE FROM players 
        WHERE p_player_key = ? 
        AND p_player_firstname = ? 
        AND p_player_lastname = ?
        AND p_player_age =  ?
    '''
    sql2 = '''
        DELETE FROM played_for 
        WHERE pf_player_key = ?
        AND pf_team_key = (select t_team_key from teams where t_team_name = ?)
        AND pf_season_key = (select se_season_key from seasons where se_season_year = ?)
        AND pf_salary = ?
    '''
    playerkey = request.json["player_key"]
    player_firstname = request.json["player_firstname"]
    player_lastname = request.json["player_lastname"]
    player_age = request.json["player_age"]
    team_name = request.json["team_name"]
    salary = request.json["salary"] 
    season_year = request.json["season_year"]
    try:
        conn = get_conn(db)
        cursor = conn.cursor()
        cursor.execute(sql1, (playerkey, player_firstname, player_lastname, player_age))
        conn.commit()
        cursor.execute(sql2, (playerkey, team_name, season_year, salary))
        conn.commit() # not sure if I need this commit
        return jsonify("success: Data Inserted")
    except Error as e:
        return jsonify(f"error: {e}")

@app.route('/insert_into_players', methods=['POST'])
def insert_into_players(): 
    sql = '''
        Insert into played_for 
        Values(?, (select t_team_key from teams where t_team_name = ?),(select se_season_key from seasons where se_season_year = ?), ?)
    '''
    playerkey = request.json["player_key"]
    player_firstname = request.json["player_firstname"]
    player_lastname = request.json["player_lastname"]
    player_age = request.json["player_age"]
    team_name = request.json["team_name"]
    salary = request.json["salary"] 
    season_year = request.json["season_year"]
    try:
        conn = get_conn(db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO players VALUES (?, ?, ?, ?)", (playerkey, player_firstname, player_lastname, player_age))
        conn.commit()
        cursor.execute(sql, (playerkey, team_name, season_year, salary))
        conn.commit() # not sure if I need this commit
        return jsonify("success: Data Inserted")
    except Error as e:
        return jsonify(f"error: {e}")

#route for Q1
@app.route('/Q1.html')
def index_Q1():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query1.sql'
    execute_query_from_file(sql_file_path, cursor)

    #cursor.execute('SELECT * FROM played_for JOIN players ON pf_player_key = p_player_key JOIN teams ON pf_team_key = t_team_key JOIN seasons ON pf_season_key = se_season_key;')

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q1.html', results=results)

#route for Q2
@app.route('/Q2.html')
def index_Q2():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query2.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q2.html', results=results)


#route for Q3
@app.route('/Q3.html')
def index_Q3():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query4.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q3.html', results=results)

#route for Q4
@app.route('/Q4.html')
def index_Q4():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query5.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q4.html', results=results)

#route for Q5
@app.route('/Q5.html')
def index_Q5():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query6.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q5.html', results=results)

#route for Q6
@app.route('/Q6.html')
def index_Q6():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query7.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q6.html', results=results)


#route for Q7
@app.route('/Q7.html')
def index_Q7():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query8.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q7.html', results=results)

#route for Q8
@app.route('/Q8.html')
def index_Q8():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query9.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q8.html', results=results)

#route for Q9
@app.route('/Q9.html')
def index_Q9():

    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query10.sql'
    execute_query_from_file(sql_file_path, cursor)

    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q9.html', results=results)

#route for Q10
@app.route('/Q10.html')
def index_Q10():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query11.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q10.html', q10=results)

#route for Q11
@app.route('/Q11.html')
def index_Q11():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query12.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q11.html', q11=results)

#route for Q12
@app.route('/Q12.html')
def index_Q12():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query13.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q12.html', q12=results)

#route for Q13
@app.route('/Q13.html')
def index_Q13():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query14.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q13.html', q13=results)

#route for Q14
@app.route('/Q14.html')
def index_Q14():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query15.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q14.html', q14=results)

#route for Q15
@app.route('/Q15.html')
def index_Q15():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query16.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q15.html', q15=results)

#route for Q16
@app.route('/Q16.html')
def index_Q16():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query18.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q16.html', q16=results)

#route for Q3
@app.route('/Q17.html')
def index_Q17():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query19.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q17.html', q17=results)

#route for Q18
@app.route('/Q18.html')
def index_Q18():
    conn = get_conn(db)
    cursor = conn.cursor()
    sql_file_path = 'sql/Queries/query20.sql'
    execute_query_from_file(sql_file_path, cursor)
    
    results = cursor.fetchall()
    close_conn(conn)

    return render_template('Q18.html', q18=results)


