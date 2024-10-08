import re

def regExWordSearch (placeHolderString, placeHolderList):
    count = 0
    for i in placeHolderList:
        if re.search(i, placeHolderString):
            count += 1
    if count == len(placeHolderList):
        return True 
<<<<<<< HEAD
    

        
                     
                     
                     
=======
>>>>>>> b84d9077eb7ed4fc4da511c30561062603d8d8bd
