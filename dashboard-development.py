#!/data/project/tools-dashboard/python/bin/python
import os
from wsgiref.handlers import CGIHandler
from app import app

app.run(debug=True)
