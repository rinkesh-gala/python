#from a file containing numbers separated by comma, print count of even numbers

with open("numbers.txt","r") as f:
    data_str=f.read()
    # list = data_str.split(",")   # split the data with comma and put it in list. and then operate on each list item and type cast to int
    counter = 0
    for i in data_str:
        if (i.isdigit() and int(i)%2==0):
            counter +=1
    print("total no. of even numbers in string are",counter)
            


