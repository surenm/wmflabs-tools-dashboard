from flask import Flask
from flask import render_template

import os
import sh
import xmltodict

from config import *

app = Flask(__name__, static_folder="./static")

if os.getenv('DEPLOYMENT') == 'development':
    app.config.from_object('app.config.DevelopmentConfig')
else:
    app.config.from_object('app.config.ProductionConfig')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/status-data")
def status_data():
    qstat = sh.Command("qstat")
    raw_jobs_xml = qstat("-u", "*", "-r", "-xml")
    return raw_jobs_xml


if __name__ == "__main__":
    app.run()