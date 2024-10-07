import requests

website=str(input("Enter Website\n > "))

if not "https://" in website:
    website="https://"+website
try:                                  # tries to fetch website
    x = requests.get(website)         # when it responds with <Response [200]>, it means it connected successfully
                                      # creates object of class "requests.models.Response"
                                            # attributes of class:
                                                # [object] .content      stores the html data of site
                                                # 
    print(x.apparent_encoding)
except:
    print("Invalid URL")
