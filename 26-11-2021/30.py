list1 = []
n = int(input("Enter the number of integers: "))
print("Enter the numbers: ")
for i in range(n):
    ele = int(input())
    if ele % 2 != 0:
        list1.append(ele)
print(list1)