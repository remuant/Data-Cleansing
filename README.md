# Data-Cleansing
A small exercise in examining a dataset to determine where cleansing is required, cleaning PLZ data and handling missing values and typos in the data.

## Table of contents
   * [Project Description](#Project-Description)
   * [Issues found in the dataset](#Issues-found-in-the-dataset)
   * [Cleansing the dataset](#Cleansing-the-dataset)
   * [Getting Started](#Getting-Started)
   * [Authors](#Authors)
   * [License](#License)
   * [Acknowledgements](#Acknowledgements)

## Project Description
A dataset must be analysed for problems and appropriately cleansed so that it can be used for data analytics purposes. 

It contains customer data with the following features:  
* **original_product_name**: Product the customer signed up to
* **postcode**: Postcode of the customer (5 digits 0-9)
* **bundesland**: The state where the customer lives
* **total_bonus**: The bonus (reduces the first year price)
* **order_date**: The date that the customer ordered the product

## Issues found in the dataset

#### Inspection of the dataset in code:
The manner in which the dataset was initially inspected is demonstrated and documented in a Jupyter Notebook [here](./1_Dataset_Inspection.ipynb).

### Invalid postcode data. 
The values for the **postcode** feature are formatted in the form of the German Postleitzahl (PLZ). These are 5 numerical digits long (0-9), sometimes with leading zeroes.
* It was found that some of the data had been rendered as a floating point number, e.g. 38120.0 instead of 38120.
* Postcodes with leading zeroes contained 4 digits rather than 5 to denote the PLZ, i.e. the leading zeros had been _pruned_ away.
* One value contained alphabetical characters.
 
### Missing data in bundesland feature
About 10% of the data instances had no value for this feature.

### Typos in the original_product_name feature
Inspection of the unique values for this feature made it apparent that errors had been made during data entry / transfer. 
This manifested as tariff names which were similar, but clearly contained an error, e.g. repeated **24**, ÖÖ instead of ÖKÖ etc. 

A check of valid tariff names was made [here](https://www.verivox.de/strom/anbieter/eon/).

## Cleansing the dataset
A Jupyter Notebook was created to show step by step how the data could be cleansed and validate the steps taken. The notebook can be viewed [here](./2_Dataset_Cleansing.ipynb).

A [script](clean_data.py) which cleanses the data has also been produced to present the code in a more compact reusable way, without the additional explanation and validation that is found in the Jupyter notebook.

### Cleaning postcode data
The following steps were taken:
* Removal of occurrences of trailing decimal points, e.g. 38120.0 -> 38120.
* Added leading zero to 4 digit PLZ postcodes.
* Removed any alphabetical characters from the postcode feature values.

### Handling missing data in bundesland feature
**Note**: it was necessary to complete cleaning of the postcode data before tackling the missing values as the PLZ values contained in the post code feature were to be used to map PLZ to Bundesland.

Mapping of PLZ to Bundesland required data in order to implement the required mapping.

#### Data set to enable mapping from PLZ to Bundesland:
* A csv file obtained from this [gist](https://gist.github.com/jbspeakr/4565964) on github was forked for this purpose. 
* It contains several features, only two were required here Plz feature and Bundesland.
* Some data had to be corrected (Schleswig-Holstein had been mispelled) and some missing PLZ data added.
* The forked and updated version used to clean the data can be found [here](https://gist.github.com/remuant/7c8f759ae4581e0bb24c6f83808d29fb). 
 *For convenience, it has also been included in this repository in the resources folder [here](./resources/German-Zip-Codes.csv).

A [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) was created using the **PLZ values as the key** and the **Bundesland as the value**.

In order to fill the missing data the dictionary was queried using the cleaned **postcode** feature data for data instances where the value for the **bundesland** feature was missing.

The value obtained was entered into the DataFrame holding the dataset.

### Correcting typos in the original_product_name feature
A dictionary was constructed with the valid tariff names as keys and a set of values for each key including the correct name and known misspellings.

The dictionary was then queried in reverse for each value of the original_product_name feature, i.e. the original feature value was used to yield the key denoting the correct tariff name.

The value obtained was entered into the DataFrame holding the dataset.

### Resulting cleaned dataset
The cleaned data was written to csv file and can be found [here](./output/cleaned_customer_data__jupyter.csv) and [here](./output/cleaned_customer_data__script.csv).

One file has been produced using the Jupyter notebook, the other with a script.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Clone this repo!

You will need **Python 3.6** or newer.

You must also install the following Python packages:

* Pandas
* jupyter

## Authors

* **remuant ;)** - *Development*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

* Information regarding E.ON tarif names sourced [here](https://www.verivox.de/strom/anbieter/eon/).

* Dataset used to link PLZ and Bundesland forked from [here](https://gist.github.com/jbspeakr/4565964).

* Modified dataset used to link PLZ and Bundesland can be accessed [here](https://gist.github.com/remuant/7c8f759ae4581e0bb24c6f83808d29fb).

* This README makes use of the template linked [here](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
