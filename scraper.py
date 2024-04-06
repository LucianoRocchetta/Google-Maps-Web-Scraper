# Scraper by Rocchetta Luciano

# Setup
import time
import random
import re # Regular expressions
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

from utils import create_dataframe
from utils import export_data

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.names = []
        self.addresses = []
        self.numbers = []
        self.emails = []
        self.websites = []
        self.ratings = []
        self.geocoders = []

    # Getting name
    def get_name(self):
        try:
            return self.driver.find_element(by=By.XPATH, value="//h1[@class='DUwDvf lfPIob']").text
        except Exception as e:
            print(e)
            return None

    def get_address(self):
        try:
            return self.driver.find_element(By.XPATH, "//button[@data-tooltip='Copiar la dirección']//div[contains(@class, 'fontBodyMedium')]").text
        except Exception as e:
            print(e)
            return None
        
    def get_number(self):
        try:
            return self.driver.find_element(By.XPATH, "//button[@data-tooltip='Copiar el número de teléfono']//div[contains(@class, 'fontBodyMedium')]").text
        except Exception as e:
            print(e)
            return None
        
    def get_website(self):
        try:
            return self.driver.find_element(By.XPATH, "//a[@data-tooltip='Abrir el sitio web']").get_attribute("href")
        except Exception as e:
            print(e)
            return None
        
    def get_rating(self):
        try:
            return self.driver.find_element(By.XPATH, "//div[@class='fontDisplayLarge']").text
        except Exception as e:
            print(e)
            return None
        
    def get_geocoder(self, url_location): # gets geographical lat/long coordinates
        try:
            coords = re.search(r"!3d-?\d\d?\.\d{4,8}!4d-?\d\d?\.\d{4,8}",
                            url_location).group()
            coord = coords.split('!3d')[1]
            return tuple(coord.split('!4d'))
        except Exception as e:
            print(e)
            return None

    def scrap(self, url):
        try:
            self.driver.maximize_window()
            self.driver.get(url=url)

            self.driver.implicitly_wait(random.randint(1, 2))

            elements = self.driver.find_elements(by=By.CLASS_NAME, value="hfpxzc")

            for element in elements:
                element.click()
                time.sleep(random.randint(1, 3))

                # Scraping info

                name = self.get_name()
                self.names.append(name)

                address = self.get_address()
                self.addresses.append(address)

                number = self.get_number()
                self.numbers.append(number)

                website = self.get_website()
                self.websites.append(website)

                rating = self.get_rating()
                self.ratings.append(rating)

                geocoder = self.get_geocoder(self.driver.current_url)
                self.geocoders.append(geocoder)

                # End scraping info
                

            time.sleep(random.randint(1, 3))

            data_df = create_dataframe(
                names=self.names, 
                addresses=self.addresses, 
                numbers=self.numbers,
                websites=self.websites,
                ratings=self.ratings,
                geocoders=self.geocoders
                )
            print(data_df)

            # Export data
            export_data(dataframe=data_df)
        
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # TESTING
    print("Testing running")

    url_test = "https://www.google.com/maps/search/pizzeria"

    scraper_test = Scraper()
    scraper_test.scrap(url=url_test)
