# save this as app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def template():
    return render_template('start.html')

@app.route("/concerts")
def concerts():
    return render_template('concerts.html')

@app.route("/actua")
def actua():
    return render_template('actua.html')

@app.route("/actua_jazz")
def actua_jazz():
    return render_template('actua_jazz.html')

@app.route("/actua_rock")
def actua_rock():
    return render_template('actua_rock.html')

@app.route("/actua_electro")
def actua_electro():
    return render_template('actua_electro.html')