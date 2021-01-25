from bs4 import * 
import os
import requests 

# Getting My Website Using requests Module
catch_website = requests.get("https://macstockofficial.blogspot.com/")

# Implementing BeautifulSoup
bs4_use = BeautifulSoup(catch_website.text, "html.parser")

# Creating All Images links containing List
images_links = []

# Getting the Images which Includes this Source Link
varfortable = bs4_use.select('img[src^="https://1.bp.blogspot.com"]')

# Appening the Links List using For Loop
for img in varfortable:
    images_links.append(img['src'])

# Creating a Folder
os.mkdir("caught_images")
i = 1

# Performing the Main function
for index, image_link, in enumerate(images_links):
    if i<=10:
        img_link = requests.get(image_link).content
        print(f"Getting Images From MacStockOfficial {catch_website}")
        with open("caught_images\\"+str(index+1)+".jpg", "wb+") as folder:
            folder.write(img_link)

        i+=1    
    else:
        folder.close()
        break
