l1=[20,40,30,10,90,15]
l2=[50,25,40,90]
print("length of list1 :",l1)
print("length of list2 :",l2)
if len(l1)==len(l2):
    print("Two lists are of same length")
total=sum(l1)
print("sum of list1 :",total)
total=sum(l2)
print("sum of list2 :",total)
if sum(l1)==sum(l2):
    print("Two lists sum is equal")
print("Value occur in  both:")
for i in l1:
    if i in l2:
        print(i)
