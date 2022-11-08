from flask import Flask, render_template, jsonify, request
import glob
import os




app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

app.run()