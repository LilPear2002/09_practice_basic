
def get_sorted_keys_values(dict_obj):
    sorted_keys = sorted(dict_obj.keys())
    sorted_values = [dict_obj[key] for key in sorted_keys]
    return [sorted_keys, sorted_values]