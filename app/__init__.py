import os
import utils
from config import *
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
    utils.error_log("hello world")
    qstat_data = utils.query_system_data(app.config['QSTAT_COMMAND'])
    vmem_data = utils.query_system_data(app.config['VMEM_COMMAND'])
    qhosts_data = utils.query_system_data(app.config['QHOSTS_COMMAND'])
    
    hosts_memory_data = utils.get_hosts_resources_data(vmem_data)
    jobs_data = utils.get_jobs_data(app.config, qstat_data)

    data = jobs_data
    return jsonify(data)

if __name__ == "__main__":
    app.run()