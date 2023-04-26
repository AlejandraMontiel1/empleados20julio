from flask import Flask
from flask import render_template

app = Flask(__name__)

#Ruteo del aplicativo
@app.router("route")
def func():