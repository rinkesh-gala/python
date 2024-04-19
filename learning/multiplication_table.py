#print multiplication table of number entered by user

table_n=int(input("enter a number whose table you want: "))
i=1
while i<=10:
    print(table_n, "x",i,"=",table_n*i)
    i +=1
