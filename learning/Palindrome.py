list1 =[1,2,2]
list2 = list1.copy()
list1.reverse()
print(list1 == list2)

#-------
#Count number of student with Grade A in following tuple 
#store the tuple in list and sort it
tup1=("A","B","C","A","A","B","D","C","B")
print(tup1.count("A"))
list_tup=list(tup1)
list_tup.sort()
print(list_tup)
