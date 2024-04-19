#print following numbers using while loop
# [1,4,9,16,25,36,49,64,81,100]

# n=1
# odd_n=1
# while n<=100:
#     print(n)
#     odd_n +=2
#     n= n+ odd_n

#search for a number X in above tuple using while loop

tup1 =(1,4,9,16,25,36,49,64,81,100)
number1=int(input("enter a number you want to search in a tuple: ")) 

counter =0

while counter < len(tup1):
    if tup1[counter]==number1:
         print ("number found at",counter,"Index" )
    counter +=1


