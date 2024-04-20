#1. search if learning word exist in practice.txt file or not. 
with open("practice.txt","r+") as f:
    data=f.read()
    if (data.find("learning") != -1): #find method will return starting index of a string. if word is not found then it will -1
        print("Found")
    else:
        print("Not Found")    

