import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
import json
import certifi
Index = 1 

URL = r"https://new.abb.com/products/2CDS211001R0164/sh201-c16"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "lxml")

prettified_html = soup.prettify()
# Write the prettified HTML to a text file
with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\output.txt', 'w', encoding='utf-8') as file:
    file.write(prettified_html)
    
# #Scrapping Image Data
    
with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\output1.txt', 'r+', encoding="utf-8") as fr:
    content = fr.read()
    y = json.loads(content)
    #lines = y.split('\n')
    for jso in y:
         print(jso["masterUrl"])
   
#https://medium.com/@joshuanishanth120/how-to-scrape-data-inside-a-shadow-dom-encapsulation-using-python-1e3320433dd9
