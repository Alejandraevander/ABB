from bs4 import BeautifulSoup
import csv
import os

Index = 1
Index_GI = 1
Index_DW = 1
Index_DS = 1
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

# #Scrapping General Information
# with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\General_Information.txt', encoding="utf8") as file_0:
#     long_description_0 = file_0.read()
#     soup = BeautifulSoup(long_description_0, 'lxml')
#     Main = soup.find_all('div',class_="col-md-4")
#     Desc = soup.find_all('div',class_="col-md-8")
#     with open(f"C:\\Users\\r14ale\\Desktop\\Scrapping_ABB\\{subfolder_name}\\General_Information.csv", mode='w', encoding='utf-8') as ContentData_0:
#         data_0 =csv.writer(ContentData_0)    
#         data_0.writerow(["Index","Item","Description"])
#         for item,desc in zip(Main,Desc):
#             Item = item.text
#             Description = desc.text
#             data_0.writerow([Index_GI,Item,Description])
#             Index_GI = Index_GI + 1
            
# #Scrapping PDF Data
# with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\DL.txt', encoding="utf8") as file_1:
#     long_description_1 = file_1.read()
#     soup = BeautifulSoup(long_description_1, 'lxml')
#     print(soup.prettify())
#     Icon_Thumbnail = soup.find_all('div', class_="dsDocument")
#     Doc_Name = soup.find_all('span', class_="dsTitle")
#     #File_Name= soup.find_all('span', class_="dsTitle")
#     #Link = soup.find_all('div', class_="dsDownloadLinks") 
#     with open(f"C:\\Users\\r14ale\\Desktop\\Scrapping_ABB\\{subfolder_name}\\Downloads.csv", mode='w', encoding='utf-8') as ContentData_1:
#         data_1 =csv.writer(ContentData_1)    
#         data_1.writerow(["Index","Icon","Doc_Name", "Doc ID", "PDF Download Link"])
#         for icon,doc in zip(Icon_Thumbnail,Doc_Name):
#             try:
#                 Icon = icon.div.img['src']
#             except:
#                 Icon = icon.div
#             Doc = doc.text
#             Doc_ID = doc.a['data-docid']
#             PDF_Link = doc.a['href']
#             data_1.writerow([Index_DW,Icon,Doc, Doc_ID, PDF_Link])
#             Index_DW = Index_DW+1
            
# #Scrapping Datasheet
with open(r'C:\Users\r14ale\Desktop\Scrapping_ABB\DS.txt', encoding="utf8") as file_2:
    long_description_2 = file_2.read()
    soup = BeautifulSoup(long_description_2, 'lxml')
    #print(soup.prettify())
    Main_Title = soup.find_all('div',class_="mt-4 ext-attr-group")
    #Main_Item = soup.find_all('div',class_="col-md-4")
    #Main_Description = soup.find_all('div',class_="col-md-8")
    with open(f"C:\\Users\\r14ale\\Desktop\\Scrapping_ABB\\{subfolder_name}\\Datasheet.csv", mode='w', encoding='utf-8') as ContentData_2:
        data_2 =csv.writer(ContentData_2)    
        data_2.writerow(["Index","Title","Item", "Description"])
        # #for titles,items,descriptions in zip(Main_Title,Main_Item,Main_Description):
        #     Title = titles.h4.text
        #     Items = items.text
        #     Description = descriptions.text
        #     data_1.writerow([Index_DS,Title,Item,Description])
        #     Index_DS = Index_DS+1
        for title in Main_Title:
            Title = title.h4.text
            Keyword = title.find_all('div',class_="row g-0 py-1 py-lg-2 border-bottom")
            for keyword in Keyword:
                Items = keyword.find_all('div',class_="col-md-4")
                Descriptions = keyword.find_all('div',class_="col-md-8")
                for Items_1,Descriptions_1 in zip(Items, Descriptions):
                    Items_final = Items_1.text
                    Descriptions_final = Descriptions_1.find_all('div',class_="d-print-none ext-attr-val")
                    for Descriptions_finalize in Descriptions_final:
                        Descriptions_Final = Descriptions_finalize.text.split("+++")
                        data_2.writerow([Index_DS,Title,Items_final,Descriptions_Final])
                        Index_DS = Index_DS+1
            
            
            
            
            
    