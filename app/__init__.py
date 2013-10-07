import os
import sys
import subprocess
import xmltodict

from config import *
from utils import error_log
from flask import Flask, render_template, jsonify


app = Flask(__name__, static_folder="./static")

if os.getenv('DEPLOYMENT') == 'development':
    app.config.from_object('app.config.DevelopmentConfig')
else:
    app.config.from_object('app.config.ProductionConfig')

environ = os.environ
environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/status-data")
def status_data():
    xml_str = subprocess.check_output(app.config['QSTAT_COMMAND'], shell = True, stderr=subprocess.STDOUT, env=environ)
    data = xmltodict.parse(xml_str)
    return jsonify(data)

if __name__ == "__main__":
    app.run()