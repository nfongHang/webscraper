import requests
entering_url=True
while entering_url:
    website=str(input("Enter Website\n > "))

    if not "https://" in website:
        website="https://"+website
    try:                                  # tries to fetch website
        x = requests.get(website)         # when it responds with <Response [200]>, it means it connected successfully
                                        # creates object of class "requests.models.Response"
                                                # attributes of class:
                                                    # .content                   stores the html data of site
                                                    # .text                      stores the html data of site, in unicode
                                                    # .apparent_encoding         holds the encoding format of text (utf-8, unicode, ASCII)   
        
        if x.status_code == 200:        # Checks if status code is 200 (connection OK)
            entering_url=False
        else:
            print('Failed to retrieve the webpage. Status code:', response.status_code)
    except:
        print("Invalid URL")
