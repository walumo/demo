from flask import Flask, request, render_template, redirect
from database.operations import delete, insert, get, next
from flask_googlemaps import get_coordinates
from dotenv import load_dotenv
import os
from sqlalchemy.orm import close_all_sessions



load_dotenv()

API_KEY = os.environ['API_KEY']

app = Flask(__name__)


#########################
#       Logging in      #
#########################

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def loginCheck():
    if request.form["username"]=="admin" and request.form["password"]=="password":
        return redirect('/showmap')
    else:
        return render_template("index.html")


#####################################################################################
#                               Google map geocoding                                #
#####################################################################################
#   -get the next job data
#   -geocode address data with get_coordinates function from flask-googlemaps:
#
#        https://github.com/flask-extensions/Flask-GoogleMaps
#   
#   -read job data and geocoded address information to list "info"
#   -render map page with info, which is read into a JS array with the help of Jinja    


@app.route("/showmap", methods=["GET", "POST"])
def showMap():
    try:
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
    except:
        return render_template("error.html")



#############################################
#   Routing for the database functions      #
#############################################

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
            return redirect('/error')  
      
@app.route("/listjobs", methods=["GET"])
def listJobs():
    try:
        joblist = get()
        close_all_sessions()
        return render_template("listjobs.html", joblist=joblist)
    except:
        return redirect('/error')

@app.route('/delete/<id>')
def delete_job(id):
    try:
        delete(id)
        close_all_sessions()
        return redirect('/listjobs')
    except:
        return redirect('/error')


#########################################
#   Rendering error in case of 'err'    #
#########################################

@app.route('/error')
def showerror():
    return render_template('error.html')


#run app
if __name__ == "__main__":
    app.run(port=5000)
