import re
from selenium import webdriver, Keys,ActionChains
from selenium.webdriver.common.by import By
#keyword search
def keyWordSearch():
    keywordList = []
    print("enter keywords")
    while True:
        # We need to put an if statement here or smth so the loop doesnt go on foreber
        keywordInput = str(input(" > "))
        if keywordInput != " ":
            keywordInput=[keywordInput]
            for i in range(len(keywordInput)):
                keywordList.append(keywordInput[i].lower())
        else: 
            break
    return keywordList

# How will the inputs happen
# We can turn this into a function in th emain body


def lookup (placeHolderString, placeHolderList):
    lookupDict={}
    unmatchedCount=0
    for i in placeHolderList:
        expression=r'[^\.]*(\b' + re.escape(i) + r'\b)[^\.]+\.?'
        print(expression)
        matches=re.findall( re.compile((expression), re.I) , placeHolderString)
        for item in matches:
            print(item)
        if matches:
            lookupDict.update({i:matches})
        else:
            message=i,"was not found in the website html. Proceed? Y/N"
            if input(message) == "N":
                return False
            else:
                unmatchedCount+=1
    print("%s words / %s words matched." % (len(placeHolderList)-unmatchedCount,len(placeHolderList)))
    return(lookupDict) 


def searchKeyWords(keyWordList, driver):
    big_string = ''
    for i in keyWordList:
        big_string += ' ' + i
    ActionChains(driver)\
    .send_keys(big_string)\
    .perform()