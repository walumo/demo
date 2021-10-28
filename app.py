# Import flask object
from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape
from database.operations import delete, insert, get


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

@app.route("/showmap", methods=["GET", "POST"])
def showMap():
    return render_template("showmap.html")


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
            return redirect('/listjobs')
        else:
            return "There was an error!"    
      
@app.route("/listjobs", methods=["GET"])
def listJobs():
    joblist = get()
    return render_template("listjobs.html", joblist=joblist)

@app.route('/delete/<id>')
def delete_job(id):
    delete(id)
    return redirect('/listjobs')

# if running directly by invoking app.py then start flask
if __name__ == "__main__":
    app.run(port=5000)
