# Electrify_Washington_Tracking_the_Rise_of_EVs

--Flask

A new folder called templates was created, inside you'll see the index.html page that displays the data from the database.
The app.py file was updated to establish the connection to sqlite database and send the result of the query:
SELECT * FROM ev_data

In the index.html you can call as many fields as needed.

In order to run the flask in your local environment once you've downloaded all the files, execute the below commands:

export FLASK_APP=app
flask run

Then the page should be available on http://127.0.0.1:5000/

--Database SQLITE 

Below you can find for your reference the steps followed to create the database ElectricVehicle.db and table ev_data as well as the import of the clean CSV file:

1. Create the database by executing command:

sqlite3 ElectricVehicle.db

2. Import the clean CSV file into ev_data table by executing command:

sqlite3
.mode csv
.import /Users/Bootcamp/projectFlask/DATA/Clean_Electric_Vehicle_Population_Data.csv ev_data

3. Review the schema by executing the below commands:

sqlite3
.schema ev_data

4. Query first 10 records:

sqlite3
select * from ev_data limit 10;

Now that you know how it was created, if you want to use the database in your local machine, download the ElectricVehicle.db and open it by executing below commands (path might change depending on where you have your project):

sqlite3
.open /Users/Bootcamp/projectFlask/ElectricVehicle.db