class Config(object):
   	BASE_URL = ''
   	QSTAT_COMMAND = ''
   	QHOSTS_COMMAND = ''
   	VMEM_COMMAND = ''
   	JOB_STAT_COMMAND = ''

class ProductionConfig(Config):
	BASE_URL = "http://tools.wmflabs.org/tools-dashboard/"
	QSTAT_COMMAND = "/usr/bin/qstat -u '*' -r -xml"
	QHOSTS_COMMAND = "/usr/bin/qhost -F h_vmem -xml"
	VMEM_COMMAND = "/usr/bin/qstat -F h_vmem -xml"
	JOB_STAT_COMMAND = "/usr/bin/qstat -xml -j {0} | sed -e 's/JATASK:[^>]*/jatask/g'" 

class DevelopmentConfig(Config):
	QSTAT_COMMAND = "cat ./sample/qstat_output.xml"
	QHOSTS_COMMAND = "cat ./sample/raw_hosts_output.xml"
	VMEM_COMMAND = "cat ./sample/vmem_output.xml"
	JOB_STAT_COMMAND = "cat ./sample/job_stat_output.xml" 
