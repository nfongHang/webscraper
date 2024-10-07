import requests
website=str(input("Enter Website\n > "))
if not "https://" in website:
    website="https://"+website
try:
    x = requests.get(website)         # when it responds with <Response [200]>, it means it connected successfully
    print(x)
except:
    print("Invalid URL")
