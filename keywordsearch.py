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
    return keyWordSearch

# How will the inputs happen
re.search()
# We can turn this into a function in th emain body