import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#keyword search
def keyWordSearch():
    keywordList = []
    print("enter keywords")
    while True:
        # We need to put an if statement here or smth so the loop doesnt go on foreber
        keywordInput = str(input("> "))
        if keywordInput != " ":
            try:
                #split multiple words in one line
                keywordInput.split(" ")
                try:
                    keywordInput.split(",")
                except:
                    pass
                print(keywordInput)
                #
                while True:
                    try:
                        keywordInput.remove("")
                    except:
                        break
            except:
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
        expression=r'[^\./<>",]*(\b' + re.escape(i) + r'\b)[^\./<>",]+\.?'
        print(expression)
        matches=re.findall( re.compile((expression), re.I) , placeHolderString)
        print(matches)
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


def searchKeyWords(keyWordList):
    big_string = ''
    for i in keyWordList:
        big_string += ' ' + i
    #entering = webdriver.find_elements_by_class_name("ant-input ant-input-lg") is there annother atrtribute we can use to fing the text box
    #entering.send_keys(big_string)
    #entering.send_keys(Keys.ENTER)


