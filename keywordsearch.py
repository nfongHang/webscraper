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
    for i in placeHolderList:
        print(i)
<<<<<<< HEAD
        if not re.search(i, placeHolderString):
            if input(i,"was not found in the website html. Proceed? Y/N") == "N":
                return False
    print("All words are within html.")
    return True 
=======
        if re.search(i, placeHolderString):
            count += 1
    print(count)
    if count == len(placeHolderList):
        return True 
>>>>>>> 73e806510457207d32a3163654a2caa752fa46dd
