def em7_message_check_file_system(p_event_message, p_target_system):
    import re
    v_is_file_system_usage_message = re.search('file system usage exceeded .* threshold', p_event_message)
    v_is_target_system_windows = p_target_system == '(Corp) Windows'
    return v_is_file_system_usage_message and v_is_target_system_windows


em7_decision_event_mapping = {
    'silo': em7_message_check_file_system
}
