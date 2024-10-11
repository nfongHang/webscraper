import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#keyword search
def keyWordSearch():
    KeywordList = []
    print("enter keywords")
    while True:
        # We need to put an if statement here or smth so the loop doesnt go on foreber
        KeywordInput = str(input("> "))
        if KeywordInput != " ":
            KeywordList.append(KeywordInput.lower())
        else: 
            break
    return KeywordList

# How will the inputs happen
# We can turn this into a function in th emain body


def regExWordSearch (placeHolderString, placeHolderList):
    for i in placeHolderList:
        print(i)
        if not re.search(i, placeHolderString):
            if input(str(i,"was not found in the website html. Proceed? Y/N")) == "N":
                return False
    print("All %s words are within html." % len(placeHolderList))
    return True 


def searchKeyWords(KeyWordList):
    big_string = ''
    for i in KeyWordList:
        big_string += ' ' + i
    #entering = webdriver.find_elements_by_class_name("ant-input ant-input-lg") is there annother atrtribute we can use to fing the text box
    #entering.send_keys(big_string)
    #entering.send_keys(Keys.ENTER)


