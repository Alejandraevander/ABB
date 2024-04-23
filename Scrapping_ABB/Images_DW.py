from bs4 import BeautifulSoup
import csv
import os

Index = 1
Index_DW = 1
# Define the parent folder path
parent_folder = r"C:\Users\r14ale\Desktop\Scrapping_ABB"

# Define the subfolder name
subfolder_name = "SH201-C16"

# Create the parent folder if it doesn't exist
if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)

try:
    # Create the subfolder inside the parent folder
    subfolder_path = os.path.join(parent_folder, subfolder_name)
    os.mkdir(subfolder_path)

    # Print a success message
    print(f"Created subfolder '{subfolder_name}' inside '{parent_folder}'.")

except:
    print("Folder already created!")

#Scrapping Image Data

# with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\Images.txt', encoding="utf8") as file:
#     long_description = file.read()
#     soup = BeautifulSoup(long_description, 'lxml')
#     #print(soup.prettify())
#     Images_Location = soup.find_all('img')
#     with open(f"C:\\Users\\r14ale\\Desktop\\Scrapping_ABB\\{subfolder_name}\\Image.csv", mode='w', encoding='utf-8') as ContentData:
#         data =csv.writer(ContentData)    
#         data.writerow(["Index","Images"])
#         for image in Images_Location:
#             Image = image['src']
#             data.writerow([Index,Image])
#             Index = Index+1


#Scrapping PDF Data
with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\DL.txt', encoding="utf8") as file_1:
    long_description = file_1.read()
    soup = BeautifulSoup(long_description, 'lxml')
    #print(soup.prettify())
    Icon = soup.find_all('div', class_="dsDocumentThumbnail")
    File_Name= soup.find_all('span', class_="dsTitle")
    Link = soup.find_all('div', class_="dsDownloadLinks") 
    