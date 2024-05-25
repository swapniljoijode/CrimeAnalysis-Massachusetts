from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import time
import os

def download_zip_files():
    # Configure download directory
    download_dir = input("Enter the download directory for this project: ")

    # Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Set up the webdriver
    s = Service('C:/Users/gjric/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe', port=9516)  # Update path to your chromedriver
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # Open the webpage
    driver.get("https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads")

    wait = WebDriverWait(driver, 20)
    crime_data_section = wait.until(EC.presence_of_element_located((By.ID, 'dwnnibrs-card')))
    print("Crime data section found.")

    # Click on the location select dropdown and choose 'Massachusetts'
    location_select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nb-select[@id='dwnnibrs-crime-loc-select']//button")))
    location_select_button.click()
    print("Location select button clicked.")

    dropdown_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//nb-option")))
    print("Dropdown options loaded.")

    # Choose 'Massachusetts' from the dropdown options
    for option in dropdown_options:
        if option.text == 'Massachusetts':
            option.click()
            print("Massachusetts selected.")
            break

    # Select the years and download the files
    years = ['2021', '2022']
    for year in years:
        try:
            # Click on the year select dropdown and choose the year
            year_select_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//nb-select[@id='dwnnibrs-crime-year-select']//button")))
            year_select_button.click()
            print(f"Year select button clicked for {year}.")

            # Wait for the dropdown options to appear and be clickable
            year_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//nb-option")))
            for option in year_options:
                if option.text == year:
                    option.click()
                    print(f"Year {year} selected.")
                    break
            #time delay to fully load the contents of the page.
            time.sleep(30)
            # Click the download button
            download_link = driver.find_element(By.XPATH, "//a[@id='dwnnibrsbtnlink']")
            print(download_link)
            download_url = download_link.get_attribute("href")
            print(download_url)

            if download_url:
                # Send a request to download the file
                response = requests.get(download_url)

                # Save the file
                file_path = os.path.join(download_dir, f"Massachusetts_{year}.zip")
                with open(file_path, "wb") as f:
                    f.write(response.content)

                print(f"Downloaded: {file_path}")
            else:
                print(f"No download link found for {year}. Skipping...")
        except Exception as e:
            print(f"Error occurred while processing year {year}: {e}")
            continue  # Skip to the next year if an error occurs

    # Close the driver
    driver.quit()

    #create a directory list to save all the zip file directories.
    dir = []
    # Verify the downloaded files
    for year in years:
        file_path = os.path.join(download_dir, f"Massachusetts_{year}.zip")  # Adjust file naming pattern
        if os.path.exists(file_path):
            print(f"Downloaded: {file_path}")
            dir.append(file_path)
        else:
            print(f"Failed to download: {file_path}")

    return dir
