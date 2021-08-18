import utility.misc_helper as mh
import utility.plz_helper as ph
import os


def create_tarif_dict():
    """
    A function which creates a dictionary for mapping typos to valid tariffs
    Returns:
    dict: A dictionary
    """
    tarif_dict = dict()
    tarif_dict['E.ON STROM'] = ('E.ON STROM')
    tarif_dict['E.ON STROM ÖKO'] = ('E.ON STROM ÖKO', 'E.ON STROM Ã–KO', 'E.ON STROM ÖO')
    tarif_dict['E.ON STROM ÖKO 24'] = ('E.ON STROM ÖKO 24')
    tarif_dict['E.ON STROM 24'] = (
    'E.ON STROM 24', 'E.ON STROM 24 24 24', 'E.ON STROM 24 24', 'E.ON STROM 24 24 24 24 24 24 24')
    tarif_dict['E.ON STROM PUR'] = ('E.ON STROM PUR')
    return tarif_dict


def clean_data():
    """
    A function which triggers cleaning of a dataset containing customer data including tariff names, and address data.
    """
    input_path = os.path.abspath('./dataset/interview_signup.csv')  # Location of the raw data
    print(input_path)
    data = ph.read_data_with_plz(input_path, 'postcode')  # Read the data in using function which preserves PLZ data
    ph.clean_postcode_plz(data, 'postcode')  # Clean postcode data with PLZ format
    ph.map_missing_bundesland_values_with_plz(data, 'bundesland', 'postcode')  # Handle missing Bundesland data
    tarif_dict = create_tarif_dict()  # Create dictionary required for processing tariff data
    # Correct the tariff data
    data['original_product_name'] = [mh.get_key_from_value(x, tarif_dict) for x in data['original_product_name']]
    output_path = './output/cleaned_customer_data__script.csv'  # Specify output path
    data.to_csv(output_path, index=False)  # Write result to csv without index, i.e. row names


if __name__ == '__main__':
    clean_data()
