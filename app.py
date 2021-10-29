# Import flask object
from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape
from database.operations import delete, insert, get, next
from flask_googlemaps import get_coordinates
from dotenv import load_dotenv
import os
from sqlalchemy.orm import close_all_sessions



load_dotenv()

API_KEY = os.environ['API_KEY']

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
        return redirect('/showmap')
    else:
        return render_template("index.html")


#################################
#   Google map functionality    #
#################################

@app.route("/showmap", methods=["GET", "POST"])
def showMap():
    next_job = next()
    address = get_coordinates(API_KEY, f'{next_job.street} " " {next_job.zipcode} " " {next_job.city}')
    lat = address["lat"]
    lon = address["lng"]
    title = next_job.job_title
    start = next_job.start_date
    desc = next_job.description
    info = [lat, lon, title, start, desc]
    close_all_sessions()
    return render_template("showmap.html", info=info)


###################################
#   Database funtions for jobs    #
###################################

@app.route("/addjob")
def addJob():
    return render_template("addjob.html")

@app.route('/newjob', methods=['GET', 'POST'])
def submit():
    if request.method=='GET':
        redirect('/addjob')
    else:
        if insert(request.form['title'], request.form['payment'], request.form['datetime'], 
                request.form['telephone'], request.form['address'], request.form['zipcode'], 
                request.form['city'], request.form['description']):
            close_all_sessions()
            return redirect('/listjobs')
        else:
            return "There was an error!"    
      
@app.route("/listjobs", methods=["GET"])
def listJobs():
    joblist = get()
    close_all_sessions()
    return render_template("listjobs.html", joblist=joblist)

@app.route('/delete/<id>')
def delete_job(id):
    delete(id)
    close_all_sessions()
    return redirect('/listjobs')

# if running directly by invoking app.py then start flask
if __name__ == "__main__":
    app.run(port=5000)
