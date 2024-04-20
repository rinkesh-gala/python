def factorial_cal(n):
    factorial_val =1
    for i in range(n,0,-1):
        factorial_val *= i
    return factorial_val

a=int(input("enter a number to find a factorial of:"))
print("factorial of",a,"is",factorial_cal(a))