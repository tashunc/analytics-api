def filter_method(variable, input_list):
    if variable in input_list:
        return True
    else:
        return False


def wrap_around_delimiter(delimiter, value):
    return delimiter + value + delimiter
