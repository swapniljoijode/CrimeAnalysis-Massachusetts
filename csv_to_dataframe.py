import pandas as pd
import os
from extractor import extract_csv_from_zip


def csv_to_dataframe():
    # Extract list of CSV files from the ZIP archive
    csv_files_list = extract_csv_from_zip()

    # Dictionary to store DataFrames for each type of CSV file
    dataframe_dict = {}

    # List of filenames to exclude from processing
    files_to_exclude = [
        "agencies",
        "NIBRS_ACTIVITY_TYPE",
        "NIBRS_ARRESTEE_GROUPB",
        "NIBRS_ARRESTEE_GROUPB_WEAPON",
        "NIBRS_ASSIGNMENT_TYPE",
        "NIBRS_BIAS_LIST",
        "NIBRS_BIAS_MOTIVATION",
        "NIBRS_DRUG_MEASURE_TYPE",
        "NIBRS_JUSTIFIABLE_FORCE",
        "NIBRS_SUSPECTED_DRUG",
        "NIBRS_SUSPECTED_DRUG_TYPE",
        "NIBRS_SUSPECT_USING",
        "NIBRS_USING_LIST"
    ]

    # Loop through each CSV file in the extracted list
    for csv_file in csv_files_list:
        # Get the base name of the file (without path)
        file_name = os.path.basename(csv_file)

        # Initialize match flag
        found_match = False

        # Check if the file name contains any of the excluded keywords
        for name in files_to_exclude:
            if name in file_name:
                found_match = True
                break  # Exit the loop once a match is found

        # If no match is found in the exclusion list, process the CSV file
        if not found_match:
            # Extract the file name without the extension
            csv_name = os.path.splitext(file_name)[0]

            # Find the index of the year in the file name (assuming '_20' precedes the year)
            year_inx = csv_name.rfind('_20')

            # Extract the base name up to the year and replace '-' with '_' for a valid DataFrame name
            df_name = csv_name[:year_inx].replace('-', '_')

            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file)

            # If the DataFrame name is not already in the dictionary, initialize an empty list for it
            if df_name not in dataframe_dict:
                dataframe_dict[df_name] = []

            # Append the DataFrame to the list associated with the DataFrame name
            dataframe_dict[df_name].append(df)

    # Return the dictionary containing lists of DataFrames
    return dataframe_dict


if __name__ == "__main__":
    # Call the function when the script is executed directly
    csv_to_dataframe()
