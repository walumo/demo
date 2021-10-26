# Import flask object
from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

#################
#   Logging in  #
#################

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def loginCheck():
    if request.form["username"]=="admin" and request.form["password"]=="password":
        return render_template("showmap.html")
    else:
        return render_template("index.html")


#################################
#   Google map functionality    #
#################################

@app.route("/showmap", methods=["POST", "GET"])
def showMap():
    return render_template("showmap.html")


###################################
#   Database funtions for jobs    #
###################################

@app.route("/addjob")
def addJob():
    return render_template("addjob.html")
      
@app.route("/listjobs")
def listJobs():
    return render_template("listjobs.html")
        


# if running directly by invoking app.py then start flask
if __name__ == "__main__":
    app.run(port=5000)
