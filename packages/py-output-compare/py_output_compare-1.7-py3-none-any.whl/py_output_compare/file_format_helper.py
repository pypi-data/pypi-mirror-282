import re


def remove_prefix_from_test(filename):
    """my test lab in formate of 1_1_lab_name

    Returns:
        _type_: file name with no 1_1_ like only lab_name
    """
    return re.sub(r"^\d+_\d+_", "", filename)
