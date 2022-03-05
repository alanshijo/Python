def facts(n):
    print("The factors of",n,"is: ")
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
n = int(input("Enter the number: "))
facts(n)