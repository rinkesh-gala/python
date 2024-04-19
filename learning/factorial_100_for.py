factorial = 1
for i in range (1,101):
    for j in range(i,0,-1):
        factorial *= j
    print (i,"factorial is",factorial)
    factorial = 1


