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


def lookup (placeHolderString, placeHolderList):
    lookupDict={}
    unmatchedCount=0
    for i in placeHolderList:
        expression='[^\.|,|"]*(\b%s\b)[^\.|,|"]+\.?' % i
        matches=re.findall( re.compile((expression), re.I) , placeHolderString)
        print(matches)
        if matches:
            lookupDict.update({i:matches})
        else:
            if input(str(i,"was not found in the website html. Proceed? Y/N")) == "N":
                return False
            else:
                unmatchedCount+=1
    print("%s words / %s words matched." % (len(placeHolderList)-unmatchedCount,len(placeHolderList)))
    return(lookupDict) 


def searchKeyWords(KeyWordList):
    big_string = ''
    for i in KeyWordList:
        big_string += ' ' + i
    #entering = webdriver.find_elements_by_class_name("ant-input ant-input-lg") is there annother atrtribute we can use to fing the text box
    #entering.send_keys(big_string)
    #entering.send_keys(Keys.ENTER)


