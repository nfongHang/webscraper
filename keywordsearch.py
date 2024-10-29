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


def lookup (placeHolderString, placeHolderList):
    for i in placeHolderList:
        print(i)
        if not re.search(i, placeHolderString):
            if input(str(i,"was not found in the website html. Proceed? Y/N")) == "N":
                return False
    print("All %s words are within html." % len(placeHolderList))
    return True 
