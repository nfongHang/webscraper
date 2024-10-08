import requests
import selenium
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import keywordsearch

entering_url=True
while entering_url:
    website=str(input("Enter Website\n > "))
# test 123
    if not "https://" in website:
        website="https://"+website
    try:                                # tries to fetch website
        x = requests.get(website)       # when it responds with <Response [200]>, it means it connected successfully
                                        # creates object of class "requests.models.Response"
                                                # attributes of class:
                                                    # .content                   stores the html data of site
                                                    # .text                      stores the html data of site, in unicode
                                                    # .apparent_encoding         holds the encoding format of text (utf-8, unicode, ASCII)   
        
        if x.status_code == 200:        # Checks if status code is 200 (connection OK)
            entering_url=False
        else:
            print('Failed to retrieve the webpage. Status code:', x.status_code)
    except:
        print("Invalid URL")

#tests scrimblo
driver = webdriver.Chrome()             # starts a virtual chrome session
driver.get(website)
gg = keywordsearch.keyWordSearch()
print(gg)