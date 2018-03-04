from flats import *
from users import *
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_googlemaps import *
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask("__main__")



GoogleMaps(app, key="YOUR_API_KEY")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def index():
	coordinates = []
	for flat in flats:
		coordinates.append({ "icon": "/static/red40.png", "lat": flat["lat"], "lng": flat["lng"], "infobox": "<a href=\"/flats/"+str(flat["id"])+"\"><div class=\"text-center\"><h6>"+ flat["address"]+"</h6><img style='width:150px;background-position:center; background-size:cover !important;' src='"+flat["imageUrl"]+"' /></div></a>"})

	return render_template("index.html", flats = flats, coordinates = coordinates, users=users)

@app.route("/login.html")
def login():
	return render_template("login.html")


@app.route("/flats/<string:id>")
def show(id):
	flat = None
	for flat in flats:
		if flat["id"] == int(id):
			flat = flat
			break
	user_found = None
	for user in users:
		if user["user_id"] == flat["user_id"]:
			user_found = user 
	return render_template("show.html", flat = flat, user = user_found, users = users)

@app.route("/add.html")
def add():
	return render_template("add.html")

if __name__ == "__main__":
	app.run(debug=True)