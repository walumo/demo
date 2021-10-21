# Import flask object
from flask import Flask, request, render_template

# import escape function to escape
from markupsafe import escape

# Create new Flask instance and place in app variable
app = Flask(__name__)

@app.route("/")
def login():
    # return string Hello World
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def loginCheck():
    if request.form["username"]=="user" and request.form["password"]=="password":
        return render_template("yobber.html")
    else:
        return render_template("index.html")
        


# if running directly by invoking app.py then start flask
if __name__ == "__main__":
    # start flask development server on port 5000
    app.run(port=5000)
