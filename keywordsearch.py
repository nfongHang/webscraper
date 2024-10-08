import re
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
    count = 0
    for i in placeHolderList:
        if re.search(i, placeHolderString):
            count += 1
    print(count)
    if count == len(placeHolderList):
        return True 
