import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import keywordsearch
def setup(link):
    driver = webdriver.Chrome()
    driver.get(link)
    return driver


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
            print('Error: Failed to retrieve the webpage. \n Status code:', x.status_code)
    except:
        print("Invalid URL")
soup = BeautifulSoup(x.text, 'html.parser')  #<--- apparently i read wrong its not for branching, nick, please read im not very sure
print(soup)                                  # something about parsing html??????? no clue



driver = setup(website)             # starts a virtual chrome session

print(keywordsearch.lookup(x.text,keywordsearch.keyWordSearch()))
 


#employ a DFS recursive function? go and search, storing all the relevant sentences and the link they are from , then open every
def linkDFS(link):
    #enter website
    setup(link)
    scrapedText=""
    # if link in website:
        #scrape link
        #scrapedText=linkDFS(scrapedLink)
    #scrape text, add to scrapedText variable
    return scrapedText






#selenium function to be able to enter in the relevant word into the 
#look into webbot instead of selenium
#be able to:
#   a: enter into search bar
#   b: wait for the books to come up
#       b2: search through all the books