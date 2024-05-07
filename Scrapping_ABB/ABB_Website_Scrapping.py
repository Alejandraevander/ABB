from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import pandas as pd
import time
import os
import csv

Index =  1

# Define your desired user agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.54"

web = "https://new.abb.com/products/2CDS211001R0164/sh201-c16"
path = r"C:\Users\r14ale\Desktop\Scrapping_ABB\\msedgedriver.exe"

#https://stackoverflow.com/questions/76377363/how-can-i-disable-personalize-your-web-experience-ms-edge-prompt-for-selenium
#Compulsory Code in Selenium 4.0
options = webdriver.EdgeOptions()
service = Service(path)

#Code to Disable the Devtools listening on ....
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--headless=new")
options.add_argument("--guest")
options.add_argument("windows-size=1920x1080")

#Open MS Edge webdriver and opening the website
driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(10)
driver.get(web)

#shadowhost = driver.find_element(By.XPATH,'//div[@class="firstrow_productcol_one"]')

# Find the element containing the shadow root
element_with_shadow_root = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.firstrow_productcol_one > pis-products-details-gallery"))
)
# Use JavaScript to access the shadow root
shadow_root = driver.execute_script("return arguments[0].shadowRoot", element_with_shadow_root)
#print(shadow_root)
# Wait for the shadow root element to be present

element_with_shadow_root = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.firstrow_productcol_one > pis-products-details-gallery"))
)
# Find all image elements
image_elements = shadow_root.find_elements(By.XPATH, "//div[contains(@class, 'pis-gallery')]//img")

# Extract src attributes and store them in a list
src_list = [element.get_attribute("src") for element in image_elements]

# Extract src attributes
#image_src_list = [element.get_attribute("src") for element in image_elements]

# Print or further process the src attributes
#for src in image_src_list:
#    print(src)