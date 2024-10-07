import re
#keyword search
KeywordList = []
print("enter keywords")
while True:
    # We need to put an if statement here or smth so the loop doesnt go on foreber
    if str(input("> ")).lower() == "\n":
        KeywordList.append(str(input("> ")).lower())

# How will the inputs happen
re.search()
# We can turn this into a function in th emain body