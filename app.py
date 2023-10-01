# app.py
#%%
#Importing Necessary Modules
import sqlite3
from flask import Flask, render_template, jsonify
import os
import json
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

@app.route('/visualization_monse.html')
def visualization_monse():
    conn = get_db_connection()

    #Execute queries to store latitude and longiitude
    c_lat = conn.execute('SELECT Lat FROM ev_data limit 1000').fetchall()
    c_lon = conn.execute('SELECT Lon FROM ev_data limit 1000').fetchall()
    #Execute queries to store electric vehicle type
    c_elecvehicle_name=conn.execute('SELECT electric_vehicle_type from (SELECT "Electric Vehicle Type" as electric_vehicle_type, count(*) as total_ev_type from ev_data group by "Electric Vehicle Type")').fetchall()
    c_elecvehicle_count=conn.execute('SELECT total_ev_type from (SELECT "Electric Vehicle Type" as electric_vehicle_type, count(*) as total_ev_type from ev_data group by "Electric Vehicle Type")').fetchall()
    #Execute queries to store model
    c_make_name=conn.execute('SELECT make from (SELECT make, count(*) as total_make from ev_data group by make) order by total_make desc').fetchall()
    c_make_count=conn.execute('SELECT total_make from (SELECT make, count(*) as total_make from ev_data group by make) order by total_make desc').fetchall()
    conn.close()

    #Serialize into JSON string latitude, longitude and electric vehicle type
    lat_results = [tuple(row) for row in c_lat]
    lat_json_string = json.dumps(lat_results)

    lon_results = [tuple(row) for row in c_lon]
    lon_json_string = json.dumps(lon_results)

    c_elecvehicle_name_results = [tuple(row) for row in c_elecvehicle_name]
    elecvehicle_name_json_string = json.dumps(c_elecvehicle_name_results)

    c_elecvehicle_count_results = [tuple(row) for row in c_elecvehicle_count]
    elecvehicle_count_json_string = json.dumps(c_elecvehicle_count_results)

    c_make_name_results = [tuple(row) for row in c_make_name]
    make_name_json_string = json.dumps(c_make_name_results)

    c_make_count_results = [tuple(row) for row in c_make_count]
    make_count_json_string = json.dumps(c_make_count_results)

    #Render index.html and pass latitude and longitude
    return render_template('visualization_monse.html', lat_json_string=lat_json_string, lon_json_string=lon_json_string, elecvehicle_name_json_string=elecvehicle_name_json_string, elecvehicle_count_json_string=elecvehicle_count_json_string, make_name_json_string=make_name_json_string, make_count_json_string=make_count_json_string)


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


#%%


if __name__ == '__main__':
    app.run(debug=True)
