str1 = input("Enter the string: ")
new = str1.split(" ")
f = new[0]
s = new[-1]
ff = f[0]
sf = s[0]
temp = ff
ff = sf
sf = temp
print("After swapping: ",ff + f[1:] + " " + sf + s[1:])

