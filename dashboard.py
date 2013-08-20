#!/data/project/tools-dashboard/python/bin/python
import site
site.addsitedir("/data/project/tools-dashboard/python/lib/python2.7/site-packages")

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)
