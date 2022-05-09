
# This is the backend of the html pages using python.

from flask import Flask, render_template, request, jsonify
import sqlite3
import os
app = Flask(__name__)

import pandas as pd

sqliteConnection = sqlite3.connect('database.db', check_same_thread=False)
cursor = sqliteConnection.cursor()
print("Database create and Successfully Connected to SQlite")
app.secret_key = "123"

app.config["UPLOAD_FOLDER1"]= "static/excel"
# You can take this route and change it to next page you want,then go to layout and add url for services.

@app.route('/')
def home():
    app.route('/')
    return render_template('/home.html')

@app.route('/upload/', methods=['POST,GET'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload']
        if upload_file.filename != '':
            file_path = os.path.join(app.config["UPLOAD_FOLDER1"], upload_file.filename)
            upload_file.save(file_path)
            data = pd.concat(pd.read_excel(file_path, sheet_name=None), ignore_index=True)
            data.to_sql('participants', cursor, if_exists='replace', index=False,)
            return render_template('search.html')

@app.route('/search/')
def search():
    return render_template('search.html')

@app.route("/search/livesearch", methods=["POST","GET"])
def livesearch():
    if request.method == "POST":
        input = request.form.get('input')
        print(input)
        Query = "SELECT * from participants WHERE name ='Melody'"
        cursor.execute(Query)
        result = cursor.fetchall()
        return jsonify(result)


app.route('/services')
def services():
    return render_template('services.html')

if __name__== '__main__':
    app.run(debug=True)






