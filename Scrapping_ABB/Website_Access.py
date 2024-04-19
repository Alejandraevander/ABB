from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import pandas as pd
import time
import os

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

#Start Code (Accept All cookies->Click on DL->Save all PDFs inside a folder allocated)
driver.find_element(By.XPATH, '//a[@id="btnSelectAllCheckboxes"]').click()
driver.find_element(By.XPATH,'//div[@data-tabname=".tab2"]').click()
time.sleep(20)


#Start Code (Go to DS->Save technical details inside multiple csv file with all the informations in a single folder for each item)

#Start Code (Go to Main Page->DL all the images link available and put inside single csv file)

