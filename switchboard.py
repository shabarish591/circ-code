import json
import os


def _airflow_request(p_event_type, p_event_dict):
    import requests
    v_config_dict = _get_config_dict()
    v_airflow_request_url = v_config_dict['airflow']['dag_urls'][p_event_type]
    try:
        print "Sending API request to Airflow DAG: '%s'" % v_airflow_request_url
         #error exception..
        response_obj = requests.post(
            v_airflow_request_url,
            headers={'rest_api_plugin_http_token': v_config_dict['airflow']['api_token']},
            data=json.dumps(p_event_dict),
            timeout=5,
            verify=False
        )
    except:
        raise

#2ND Function
def _em7_message_check_file_system(p_event_message, p_target_system):
    import re
    #error exception
    v_is_file_system_usage_message = re.search('file system usage exceeded .* threshold', p_event_message)
    v_is_target_system_windows = p_target_system == '(Corp) Windows'
    return v_is_file_system_usage_message and v_is_target_system_windows


def _get_config_dict(p_config_file_name="config.json"):
    from os.path import dirname, realpath
     #error exception
    v_config_file = "%s/auto-tiger/json/%s" % (dirname(realpath(__file__)), p_config_file_name)
    try:
        with open(v_config_file) as config_file:
            v_config_file_dict = json.load(config_file)
        return v_config_file_dict[os.environ.get('ENV', 'dev')]
    except:
        raise


def handler(p_event, context):
    print "Event payload: %s" % str(p_event)
    em7_decision_event_mapping = {
        'silo': _em7_message_check_file_system
    }

    v_message = p_event['event'].get('event_message', None).lower()
    v_org = p_event['event'].get('organization', None)
    v_decision_case_found = False
    for v_em7_event_type, v_decision_func in em7_decision_event_mapping.iteritems():
        if v_decision_func(v_message, v_org):
            _airflow_request(v_em7_event_type, p_event['event'])
            v_decision_case_found = True
            break
    if not v_decision_case_found:
        print "Given event payload does not match a current use case:\n %s" % str(p_event['event'])
