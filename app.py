"""
    test a SQLite database connection locally
    assumes the database file is in same location
    as this .py file
"""
from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error
from sqlalchemy import text
import requests
import json


app = Flask(__name__, template_folder='Template', static_folder="static")
# #database conenction
# connection = mysql.connector.connect(host='aws.connect.psdb.cloud',\
#                                          database='database_work',\
#                                          user='dvt52fi4x22vvzuigz3v',\
#                                          password='pscale_pw_Rjk0JwWEW0qoEWn4S2zTUAHHsCvaAIldDCxiZkSI9f8')
# cursor = connection.cursor()
# cursor.execute("select * from database_work.travel_location;")
# # get all records
# records = cursor.fetchall()

response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=8ddbc01df6caa3c70f7bbc06d87e1331")
print(response.text)

@app.route('/')
def home_page():
    return render_template("first.html")


@app.route('/jobs/<id>')
def travel_page(id):
    cursor.execute("select * from database_work.travel_location where id = id;")
    return dict( cursor)

if __name__ == '__main__':
    app.run(debug=True)

