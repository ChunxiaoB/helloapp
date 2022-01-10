from flask import Flask
from flask import request
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route("/")
def index():
    # return "Congratulations, it's a web app!"
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
            """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
              </form>"""
            + "Fahrenheit: "
            + fahrenheit
            )


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


@app.route("/login")
def login():
    # login page
    username = request.args.get("username", "")
    if username:
        greeting = "Hello " + username + "!"
    else:
        greeting = "Hello World!"
    return (
            """<form action="" method="get">
                User Name: <input type="text" name="username">
                <input type="submit" value="Submit">
              </form>"""
            + greeting
    )


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/user_input")
def user_input():
    return render_template("user_input.html")




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
