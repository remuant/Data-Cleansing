def get_key_from_value(value, dictionary):
    list_of_keys = [key
                for key, list_of_values in dictionary.items()
                if value in list_of_values]
    if list_of_keys:
        return list_of_keys[0]
    else:
        return ''
    