#print list using recursion

def print_list(list1, index=0):
    if (index==len(list1)):
        return
    else:
        print(list1[index])
        print_list(list1, index+1)


list2= [1,2,3,4,5]
print_list(list2)