def add(str1):
    l = str1[-3:]
    if l == "ing":
        print("After adding: ", str1 + "ly")
    else:
        print("After adding: ", str1 + "ing")
str1 = input("Enter the string: ")
add(str1)
