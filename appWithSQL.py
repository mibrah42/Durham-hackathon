import os

from flask import Flask, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask("__main__")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine('postgres://hivgnadr:rCYJuF9NSdcHkiySVzOXunfjy2EFD48B@stampy.db.elephantsql.com:5432/hivgnadr')
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
	flats = db.execute("SELECT * FROM flats;").fetchall()
	return render_template("index.html", flats = flats)

@app.route("/login.html")
def login():
	return render_template("login.html")


if __name__ == "__main__":
	app.run(debug=True)