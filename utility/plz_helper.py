"""
A collection of functions for inspecting and cleansing data using PLZ.

@author: remuant
"""

import re

def check_invalid_plz_format(text):
    """
    A function which checks whether a String is a valid PLZ.
    Args:
    	text (string): A string denoting the PLZ
    Returns: 
	bool: A boolean indicating whether the text provided is an invalid PLZ (invalid=True)
    """
    search_condition_1 = r'(?<!\d)\d{5}(?!\d)'
    search_condition_2 = r'\b\d{5}\b'
    if re.search(search_condition_2, text):
        return False
    else:
        return True
