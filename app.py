#Create a new dir eg ev_data_showcase,  Inside this directory, create a new Python file named "app.py".
# This will be the main Flask application file.

# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
