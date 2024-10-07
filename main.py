import requests

website=str(input("Enter Website\n > "))

if not "https://" in website:
    website="https://"+website
try:                                  # tries to fetch website
    x = requests.get(website)         # when it responds with <Response [200]>, it means it connected successfully
    print(type(x))                          #
except:
    print("Invalid URL")
