list1 = []
n = int(input("Enter the number of integers: "))
print("Enter the integers: ")
for i in range(n):
    ele = int(input())
    if ele > 100:
        list1.append("Over")
    else:
        list1.append(ele)
print(list1)