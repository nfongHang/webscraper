import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import Keys
from urllib.request import urlopen
import keywordsearch
entering_url=True
while entering_url:
    website=str(input("Enter Website\n > "))

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
soup = BeautifulSoup(x.text, 'html.parser')  #<--- apparently i read wrong its not for branching, nick, please read im not very sure
# apparently its for pulling HTML files
# It works just fine I think?
print(soup)                                  # something about parsing html??????? no clue
keywords = keywordsearch.keyWordSearch()
#tests 
driver = webdriver.Chrome()             # starts a virtual chrome session
driver.get(website)
keywordsearch.regExWordSearch(x.text,keywords)
keywordsearch.searchKeyWords(keywords)
#asdf
#sdfghjggjfhahgj

# I think theres a selenium function which allows for accessing the web page with the code like going onto the search bar
# This might solve one of the problems