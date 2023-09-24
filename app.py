#Create a new dir eg ev_data_showcase,  Inside this directory, create a new Python file named "app.py".
# This will be the main Flask application file.

# app.py
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('ElectricVehicle.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    evdata = conn.execute('SELECT * FROM ev_data').fetchall()
    conn.close()
    return render_template('index.html', evdata=evdata)

if __name__ == '__main__':
    app.run(debug=True)
