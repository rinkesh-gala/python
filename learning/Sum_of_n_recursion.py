#sum of n number using recursion

def sum_recur(n):
    if (n==0):
        return 0
    return sum_recur(n-1) + n

a= int(input("enter a number: "))
print("sum of first",a,"number is",sum_recur(a))
