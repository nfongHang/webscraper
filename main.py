import requests

website=str(input("Enter Website\n > "))

if not "https://" in website:
    website="https://"+website
try:                                  # tries to fetch website
    x = requests.get(website)         # when it responds with <Response [200]>, it means it connected successfully
                                      # creates object of class "requests.models.Response"
                                            # attributes of class:
                                                # .content                   stores the html data of site
                                                # .apparent_encoding         holds the encoding format of text (utf-8, unicode, ASCII)   
    print(x.url)
except:
    print("Invalid URL")
