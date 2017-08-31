def convert_json_data(p_event_dict):
    import json
    import urllib
    v_event_dict = dict()
    for k,v in p_event_dict.iteritems():
        v_event_dict[k] = v.replace(' ','_')
    v_event_str = json.dumps(v_event_dict, separators = (',',':'))
    print "Converted event payload: %s" % v_event_str
    v_event_encoded = urllib.quote(v_event_str)
    print "URL encoded event payload: %s" % v_event_encoded
    return v_event_encoded


def api_get(p_event_type, p_event_dict):
    import requests
    import auto_tiger_aws.src.util as util
    v_config_dict = util.get_config_dict()
    v_airflow_request_url = v_config_dict['airflow']['dag_urls'][p_event_type]
    try:
        print "Sending API request to Airflow DAG: '%s'" % v_airflow_request_url
        response_obj = requests.get(
            v_airflow_request_url + '&conf=' + convert_json_data(p_event_dict),
            headers={'rest_api_plugin_http_token': v_config_dict['airflow']['api_token']},
            timeout=5,
            verify=False
        )
        print "Response object: %s" % response_obj.json()
    except:
        raise
