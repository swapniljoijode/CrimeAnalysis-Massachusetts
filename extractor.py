import zipfile
from download_files_from_web import download_zip_files
import os
import re

def extract_csv_from_zip():
    zip_files = download_zip_files()

    extract_to_folder = input("Enter the folder to extract the csv files to: ")

    csv_file_dir = []

    for zip_path in zip_files:
        if not zip_path.endswith('.zip'):
            print("Please enter a valid zip file")
        else:
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
                            file_name = os.path.basename(file)
                            extracted_path = os.path.join(extract_to_folder, file_name)
                            with zip_ref.open(file) as source, open(extracted_path, 'wb') as target:
                                with source, target:
                                    target.write(source.read())
                            csv_index = file_name.rfind('.csv')
                            csv_name = ''
                            if csv_index != -1:
                                csv_name = file_name[:csv_index]
                            else:
                                None
                            new_csv_name = csv_name + '_'+ year + '.csv'
                            new_file_path = os.path.join(extract_to_folder, new_csv_name)
                            os.rename(extracted_path, new_file_path)
                            csv_file_dir.append(new_file_path)
                            print(f"Extracted: {file}")

                print("CSV files extracted successfully.")
                #return "CSV files extracted successfully."
            except Exception as e:
                print(f"Error extracting CSV files: {e}")
                #return f"Error extracting CSV : {e}"
    return csv_file_dir

if __name__ == '__main__':
    extract_csv_from_zip()





