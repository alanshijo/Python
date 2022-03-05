lst=[]
s = 0
n = int(input("Enter the limit: "))
print("Enter the elements: ")
for i in range(n):
    ele = int(input())
    lst.append(ele)
    s = s + ele
print("The list is",lst)
print("Sum of all elements of the list: " , s)