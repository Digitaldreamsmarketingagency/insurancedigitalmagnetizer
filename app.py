from flask import Flask, request, render_template, send_file, session, redirect
import sqlite3 as sql
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def abouty():
    return render_template("about.html")

@app.route("/contact")
def contacty():
    return render_template("contact.html")

@app.route("/RESP")
def respy():
    return render_template("resp.html")

@app.route("/our-team")
def team_our():
    return render_template("team.html")

@app.route("/photo-galary")
def photo_gal():
    return render_template("photog.html")

@app.route("/llqp-classes")
def llqp_classes():
    return "Coming Soon..."

@app.route("/join-us")
def join_us():
    return render_template("join.html")

@app.route("/our-commercials")
def comercials():
    return render_template("comersi.html")


# insurances #######################################################################

@app.route('/life/<id>')
def lify(id):
    a = "/pages/life/" + id + ".html"
    return render_template(a)

@app.route('/investments/<id>')
def investy(id):
    a = "/pages/investments/" + id + ".html"
    return render_template(a)

@app.route('/travel/<id>')
def travely(id):
    a = "/pages/travel/" + id + ".html"
    return render_template(a)

@app.route('/online/<id>')
def onliney(id):
    a = "/pages1/online/" + id + ".html"
    return render_template(a)

@app.route('/super/<id>')
def supery(id):
    a = "/pages1/super/" + id + ".html"
    return render_template(a)

#
#   ddd         a       tttttttttt        a
#   d   d      a  a          t           a  a
#   d    d    aaaaaa         t          aaaaaa
#   d   d    a      a        t         a      a
#   ddd     a        a       t        a        a

@app.route("/store-data/<id>", methods=['GET','POST'])
def datay(id):
    a = []
    if request.method == 'POST':
        for i in request.form:
            a.append(request.form.get(i))
        a.append(datetime.now().time().strftime("%H:%M:%S"))
        a.append(datetime.now().date().strftime("%d/%m/%Y"))
        try:
            with open(id+".csv","r") as aa:
                aa
            with open(id+".csv","a") as ae:
                writer = csv.writer(ae)
                writer.writerow(a)
        except:
            with open(id+".csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(a)
        return render_template("done.html")
    else:
        return render_template("index.html")

@app.route("/datas/get-data/<id>", methods=['GET','POST'])
def gety(id):
    return send_file(id+".csv")

@app.route("/datas/<id>", methods=['GET','POST'])
def datas(id):
    a = []
    if "id" in session:
        try:
            with open(id+".csv","r") as aa:
                for i in aa:
                    a= i
        except:
            pass
        return render_template("data.html",d=int(id))
    else:
        return render_template("admin.html")
    
@app.route("/check-id", methods=['POST'])
def getid():
    if request.form.get('p') == "qpalzm@":
        session["id"] = "admin"
        return redirect("/datas/5")
    else:
        return "worng password"