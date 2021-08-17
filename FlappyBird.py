from flask import Flask, request, redirect, url_for, render_template, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import requests
from bs4 import BeautifulSoup

app = Flask (__name__)

@app.route('/')
def loadgame():
    return render_template('FlappyBird.html')

app.run(debug=True)