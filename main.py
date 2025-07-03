# main.py
import os
import base64
import io
import math
import random
import shutil
import hashlib
import datetime
import calendar
import argparse
import urllib.request
import urllib.parse
import webbrowser
import requests
import inspect

from random import randint
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
from camera import VideoCamera
from camera1 import VideoCamera1
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from PIL import Image
from skimage import transform
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imagehash
import joblib
import mysql.connector

# Load environment variables
load_dotenv()

# Database connection using .env
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    charset="utf8"
)

app = Flask(__name__)
app.secret_key = 'abcdef'  # You may also move this to .env if needed

UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---- ROUTES ----

@app.route('/', methods=['GET', 'POST'])
def index():
    open("lang.txt", "w").close()
    return render_template('index.html', msg="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('admin'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Add your remaining routes and refactor similarly...

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
