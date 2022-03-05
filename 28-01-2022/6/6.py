import csv
a  =open("desp.csv","r")
b = open("copy.txt", "w")
c = a.readlines()
d = len(c)
for i in range(0,d):
    if i<5:
         g = b.write(c[i])
b.close()
b = open("copy.txt", "r")
k = b.readlines()
print(k)