class Config(object):
   	BASE_URL = ''

class ProductionConfig(Config):
	BASE_URL = "http://tools.wmflabs.org/tools-dashboard/"

class DevelopmentConfig(Config):
	pass
