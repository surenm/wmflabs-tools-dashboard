class Config(object):
   	BASE_URL = ''
   	QSTAT_COMMAND = ''

class ProductionConfig(Config):
	BASE_URL = "http://tools.wmflabs.org/tools-dashboard/"
	QSTAT_COMMAND = "/usr/bin/qstat -u '*' -r -xml"

class DevelopmentConfig(Config):
	QSTAT_COMMAND = "cat ./sample/qstat_output.xml"
