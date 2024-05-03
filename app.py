# save this as app.py
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def template():
    return render_template('start.html')

@app.route("/concerts")
def concerts():
    return render_template('concerts.html')

@app.route("/actua")
def actua():
    f = open('static/actua.json')
    data = json.load(f) 
    f.close()
    return render_template('actua.html', summary = data)

@app.route("/actua_jazz")
def actua_jazz():
    f = open('static/actua.json')
    data = json.load(f) 
    f.close()
    return render_template('actua_jazz.html', summary = data)

@app.route("/actua_rock")
def actua_rock():
    f = open('static/actua.json')
    data = json.load(f) 
    f.close()
    return render_template('actua_rock.html', summary = data)

@app.route("/actua_electro")
def actua_electro():
    f = open('static/actua.json')
    data = json.load(f) 
    f.close()
    return render_template('actua_electro.html', summary = data)