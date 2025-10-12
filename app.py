from flask import Flask, request
import sqlite3

app = Flask(__name__)
DB_NAME = 'app.db'

# VULNERABLE FUNCTION: Prone to SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    # Insecure query construction
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT * FROM users WHERE id = '%s'" % user_id 
    cursor = conn.execute(query)
    
    return str(cursor.fetchall())
