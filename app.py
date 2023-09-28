# app.py
#%%
#Importing Necessary Modules
import sqlite3
from flask import Flask, render_template, jsonify
import os
#%%

#Setting Up the Flask App
currentdirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
#%%

#Creating SQLite Database Connection Function(connecting back end)
def get_db_connection():
    conn = sqlite3.connect('ElectricVehicle.db')
    conn.row_factory = sqlite3.Row
    return conn
#%%

#Defining Routes and View Functions(rendering frontend)
@app.route('/')
def index():
    conn = get_db_connection()
    evdata = conn.execute("SELECT DISTINCT Make FROM ev_data").fetchall()
    conn.close()
    return render_template('index.html', evdata=evdata)

@app.route('/ev/<string:make>')
def ev_make(make):
    conn = get_db_connection()
    evmodels = conn.execute('SELECT * FROM ev_data WHERE Make = ?', (make,)).fetchall()
    conn.close()

    if not evmodels:
        return render_template('404.html'), 404

    return render_template('detail.html', evmodels=evmodels)

## Testing API on Kathia's html   !DELETE ME!
#%%
@app.route('/api/evdata', methods=['GET'])
def api_ev_data():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM ev_data").fetchall()
    conn.close()
    data_dict_list = [dict(row) for row in data]
    return jsonify(data_dict_list)

# Add a new route for the visualization page
@app.route('/visualization')
def visualization():
    return render_template('visualization.html')
#%%


if __name__ == '__main__':
    app.run(debug=True)
