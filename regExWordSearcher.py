import re

def regExWordSearch (placeHolderString, placeHolderList):
    count = 0
    for i in placeHolderList:
        if re.search(i, placeHolderString):
            count += 1
    if count == len(placeHolderList):
        return True 
    

        
                     
                     
                     
