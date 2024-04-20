#print line number where the word is found
def check_file ():
    with open("practice.txt","r") as f:
        line = True
        word = "learning"
        counter = 1
        while (line != ""): # end of file file means blank/empty string is returned. if there are empty lines between two setence 
            line = f.readline() # it will return \n
            if word in line:
                return counter 
            counter +=1
        return -1
    
print(check_file())
        
        
        





    