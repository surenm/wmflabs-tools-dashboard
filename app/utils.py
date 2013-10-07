import os
import sys
import pprint
import subprocess
import xmltodict

environ = os.environ
environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'

def error_log(str):
    error_file = open('./logs/error.log', 'a')
    error_file.write(str)
    error_file.write("\n")
    error_file.close()

def query_system_data(command):
    raw_system_str = subprocess.check_output(command, shell = True, stderr=subprocess.STDOUT, env=environ)
    data = xmltodict.parse(raw_system_str)
    return data

def get_hosts_resources_data(vmem_data):
    hosts_data = {}

    hosts_list = vmem_data['job_info']['queue_info']['Queue-List']
    for host in hosts_list:
        server_name = host['name'].split('@')[-1]
        if server_name:
            hosts_data[server_name] = host['resource']['#text']

    return hosts_data

def get_jobs_data(config, qstat_data):
    jobs_stats_data = {}

    jobs_list = qstat_data['job_info']['queue_info']['job_list']

    for job in jobs_list:
        job_id = job['JB_job_number']
        error_log("Inspecting Job: " + job_id)
        detailed_job_stats_command = config['JOB_STAT_COMMAND'].format(job_id)
        raw_detailed_job_stats_data = query_system_data(detailed_job_stats_command)
        detailed_stats_data = raw_detailed_job_stats_data['detailed_job_info']['djob_info']['element']

        job_stats = {}

        job_stats['tool'] = detailed_stats_data['JB_owner']
        job_stats['job_submission_time'] = detailed_stats_data['JB_submission_time']
        job_stats['name'] = detailed_stats_data['JB_job_name']

        for key, value in detailed_stats_data['JB_hard_resource_list'].iteritems():
            if value['CE_name'] == 'h_vmem':
                job_stats['mem_allocated'] = float(value['CE_doubleval'])/1048576;
        
        job_stats['tasks'] = 0
        job_stats['mem_used'] = 0
        job_stats['mem_max'] = 0
        job_stats['cpu'] = 0

        job_stats['state'] = job['state']
        job_stats['start'] = job['JAT_start_time']
        job_stats['slots'] = job['slots']
        job_stats['host'] = job['queue_name'].split('@')[-1]
        job_stats['queue'] = job['queue_name'].split('@')[0]
    
        for key, task in detailed_stats_data['JB_ja_tasks'].iteritems():

            job_stats['tasks'] = job_stats['tasks'] + 1
            for resource in task['JAT_scaled_usage_list']['scaled']:
                for resource_name, resource_value in resource.iteritems():
                   if resource_name == 'cpu':
                       job_stats['cpu'] += resource_value
                   elif resource_name == 'vmem':
                       job_stats['mem_used'] = float(resource_value)/1048576
                   elif resource_name == 'maxvmem':
                       job_stats['mem_max'] = float(resource_value)/1048576

        jobs_stats_data[job_id] = job_stats

    return jobs_stats_data