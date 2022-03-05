str1 = input("Enter the string: ")
print("The string is:", str1)
f = str1[0]
str1 = str1.replace(f, '$')
str1 = f + str1[1:]
print("The string after replaced:", str1)
