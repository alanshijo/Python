n=int(input("Enter the limit:"))
n1=0
n2=1
s=0
print("fibonacci series:")
print(n1)
print(n2)
for i in range(1,n-1):
    s=n1+n2
    n1=n2
    n2=s
    print(s)