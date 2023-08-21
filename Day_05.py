def printPattern(n):
    for i in range (n):
        for j in range(n):
            if i == j or i+j == n-1:
                print(i+1,end='')
            else:
                print("",end='')
            print()

printPattern(5)