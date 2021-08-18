"""
A collection of functions for inspecting and cleansing data using PLZ.

@author: remuant
"""

import re
import pandas as pd
import os

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


def contains_letter_number(text):
    """
    A function which checks whether a String contains at least one letter and number
    Args:
        text (string): A string
    Returns:
    bool: A boolean indicating whether the text provided contains at least one letter and number
    """
    # https://stackoverflow.com/questions/64862663/how-to-check-if-a-string-is-strictly-contains-both-letters-and-numbers
    return text.isalnum() and not text.isalpha() and not text.isdigit()


def read_data_with_plz(input_path, feature_name_plz):
    """
    A function which reads data containing a feature with PLZ formatted data and ensures that leading zeroes are
    preserved.
    Args:
        input_path (string): A string specifying the location of the csv dataset
        feature_name_plz (string): A string specifying the feature name containing PLZ formatted data.
    Returns:
    DataFrame: A DataFrame
    """
    #Note: A converter is necessary when reading in the postcode data in order to ensure
    #      that any leading zeroes are preserved.
    df = pd.read_csv(input_path, converters={feature_name_plz: lambda x: str(x)})
    return df


def clean_postcode_plz(df, feature_name):
    """
    A function which cleans the feature values for PLZ formatted data by removing .0, restoring leading zeroes and
    removing any alphabetical characters.
    Args:
        df (DataFrame): A DataFrame containing a column of PLZ formatted data to be cleaned
        feature_name (string): A string denoting the name of the column containing PLZ formatted data
    """
    df[feature_name] = df[feature_name].astype(str).replace('\.0', '', regex=True)
    df[feature_name] = [re.sub("[^0-9]", "", x) for x in df[feature_name]]
    df[feature_name] = [x.zfill(5) for x in df[feature_name]]#'postcode'


def map_missing_bundesland_values_with_plz(df, feature_name_bl, feature_name_plz):
    """
    A function which adds missing Bundesland values using available PLZ data.
    Args:
        df (DataFrame): A DataFrame containing a column with missing Bundesland data
        feature_name_bl (string): A string denoting the name of the column with missing Bundesland data
        feature_name_bl (string): A string denoting the name of the column containing complete and correct PLZ
        formatted data
    """
    plz_csv_path = os.path.abspath('./resources/German-Zip-Codes.csv')  # Location of data required for mapping
    print(plz_csv_path)
    plz_data = pd.read_csv(plz_csv_path, sep=';', converters={'Plz': lambda x: str(x)})  # Read in the mapping data
    my_plz_dict = dict(zip(plz_data.Plz, plz_data.Bundesland))  # Create dictionary
    # Perform mapping from PLZ to Bundesland where bundesland data value are missing
    df[feature_name_bl] = [my_plz_dict[y] if pd.isnull(x) else x for x, y in zip(df[feature_name_bl], df[feature_name_plz])]
