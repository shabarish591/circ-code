import json


def get_config_dict(p_config_file_name="config.json"):
    import os
    from os.path import dirname, realpath
    v_config_file = "%s/auto_tiger_aws/json/%s" % (dirname(dirname(realpath(__file__))), p_config_file_name)
    try:
        with open(v_config_file) as config_file:
            v_config_file_dict = json.load(config_file)
        return v_config_file_dict[os.environ.get('ENV', 'dev')]
    except:
        raise


def get_kinesis_data_list(p_kinesis_payload):
    import base64
    return [
        json.loads(base64.b64decode(v_kinesis_record_dict['kinesis']['data']))
        for v_kinesis_record_dict in p_kinesis_payload.get('Records', [])
    ]
