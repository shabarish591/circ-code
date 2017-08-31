def handler(p_event, context):
    import auto_tiger_aws.src.util as util
    import auto_tiger_aws.src.airflow as airflow
    from auto_tiger_aws.src.switchboard.decision_functions import em7_decision_event_mapping

    print "Event payload: %s" % str(p_event)
    for v_event_dict in util.get_kinesis_data_list(p_event):
        v_message = v_event_dict['event'].get('event_message', None).lower()
        v_org = v_event_dict['event'].get('organization', None)
        v_decision_case_found = False
        for v_em7_event_type, v_decision_func in em7_decision_event_mapping.iteritems():
            if v_decision_func(v_message, v_org):
                airflow.api_get(v_em7_event_type, v_event_dict['event'])
                v_decision_case_found = True
                break
        if not v_decision_case_found:
            print "Given event payload does not match a current use case: %s" % str(v_event_dict['event'])
