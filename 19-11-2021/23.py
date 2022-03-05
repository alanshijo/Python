n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if n1 > n2 and n1 > n3:
    print("n1 :" , n1 , "is bigger")
elif n2> n1 and n2 >n3:
    print("n2 :" , n2 , "is bigger")
else:
    print("n3 :" , n3 , "is bigger")