
from flask import Flask, render_template, request, redirect, url_for, session, json, jsonify
import json


app = Flask(__name__)

# read file
with open('data_source.json', 'r') as myfile:
    data = myfile.read()

    # python object to be appended
y = {"student_name":"Han Li",
     "signup_date": "01/22/2022"
     }


@app.route("/display_json")
def display_json_in_table():
    data = json.load(open("data_source.json"))
    #return render_template('display_json.html', title="DISPLAY JSON DATA IN HTML", jsondata=json.dumps(data))
    return render_template('display_json.html', title="DISPLAY JSON DATA IN HTML", jsondata=data["signup_details"])


@app.route("/add", methods = ['POST', 'GET'])
# function to add to JSON
# return display_json.html with new data
# that contain
def write_json(filename='data_source.json'):
    if request.method == 'POST':
        new_data = request.form
    #return render_template('result.html', result = new_data)

    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["signup_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

        # final step: display the json with new data in html
        return render_template('display_json.html', title="DISPLAY JSON DATA IN HTML", jsondata=file_data["signup_details"])


@app.route("/")
def signup():
    return render_template('signup.html')





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)