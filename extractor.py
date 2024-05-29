import zipfile
from download_files_from_web import download_zip_files
import os
import re


def extract_csv_from_zip():
    # Download ZIP files using the provided function
    zip_files = download_zip_files()

    # Ask the user for the folder to extract CSV files to
    extract_to_folder = input("Enter the folder to extract the csv files to: ")

    # List to store paths of extracted CSV files
    csv_file_dir = []

    # Loop through each ZIP file path in the downloaded list
    for zip_path in zip_files:
        # Ensure the file is a ZIP file
        if not zip_path.endswith('.zip'):
            print("Please enter a valid zip file")
        else:
            # Extract the year from the ZIP file name using regular expression
            year = re.search(r'(\d{4})', zip_path).group(1)
            try:
                # Ensure the extraction directory exists
                if not os.path.exists(extract_to_folder):
                    os.makedirs(extract_to_folder)

                # Open the ZIP file
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # List all files in the ZIP archive
                    for file in zip_ref.namelist():
                        # Check if the file is a CSV
                        if file.endswith('.csv'):
                            # Get the base name of the file (without path)
                            file_name = os.path.basename(file)
                            # Define the path to extract the file to
                            extracted_path = os.path.join(extract_to_folder, file_name)
                            # Extract and save the file
                            with zip_ref.open(file) as source, open(extracted_path, 'wb') as target:
                                target.write(source.read())

                            # Modify the extracted file name to include the year
                            csv_index = file_name.rfind('.csv')
                            csv_name = file_name[:csv_index] if csv_index != -1 else ''
                            new_csv_name = csv_name + '_' + year + '.csv'
                            new_file_path = os.path.join(extract_to_folder, new_csv_name)
                            # Rename the file to include the year
                            os.rename(extracted_path, new_file_path)
                            # Append the new file path to the list of CSV files
                            csv_file_dir.append(new_file_path)
                            print(f"Extracted: {file}")

                print("CSV files extracted successfully.")
            except Exception as e:
                print(f"Error extracting CSV files: {e}")

    # Return the list of extracted CSV file paths
    return csv_file_dir


if __name__ == '__main__':
    # Call the function when the script is executed directly
    extract_csv_from_zip()
