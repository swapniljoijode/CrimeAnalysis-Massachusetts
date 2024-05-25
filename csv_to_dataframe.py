import pandas as pd
import os
from extractor import extract_csv_from_zip

def csv_to_dataframe():
    csv_files_list = extract_csv_from_zip()

    dataframe_dict = {}

    files_to_exclude = ["agencies",
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
    "NIBRS_USING_LIST"]

    for csv_file in csv_files_list:
        file_name = os.path.basename(csv_file)
        found_match = False
        for name in files_to_exclude:
            if name in file_name:
                found_match = True
                break  # Once a match is found, no need to continue checking with other strings
        if not found_match:
            # If no match found, convert the CSV to a DataFrame
            csv_name = os.path.splitext(file_name)[0]  # Extracting the file name without extension
            year_inx = csv_name.rfind('_20')
            df_name = csv_name[:year_inx]
            df_name = df_name.replace('-', '_')  # Replacing '-' with '_' for valid DataFrame name
            df = pd.read_csv(csv_file)
            if df_name not in dataframe_dict:
                dataframe_dict[df_name] = []
            dataframe_dict[df_name].append(df)
    return dataframe_dict

if __name__ == "__main__":
    csv_to_dataframe()