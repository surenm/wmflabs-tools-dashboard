#!/data/project/tools-dashboard/python/bin/python
import site
site.addsitedir("/data/project/tools-dashboard/python/lib/python2.7/site-packages")

import sys
sys.stderr = open('./logs/error.log', 'w')

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)

