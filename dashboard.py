#!/data/project/tools-dashboard/python/bin/python
import site
site.addsitedir("/data/project/tools-dashboard/python/lib/python2.7/site-packages")

from wsgiref.handlers import CGIHandler
from werkzeug.debug import DebuggedApplication
from app import app

app = DebuggedApplication(app, evalex=True)

CGIHandler().run(app)

