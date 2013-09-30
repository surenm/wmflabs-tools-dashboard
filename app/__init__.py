from flask import Flask
from flask import render_template

import os
from config import *

app = Flask(__name__, static_folder="./static")

if os.getenv('DEPLOYMENT') == 'development':
	app.config.from_object('app.config.DevelopmentConfig')
else:
	app.config.from_object('app.config.ProductionConfig')
	
@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()