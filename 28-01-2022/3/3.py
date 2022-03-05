import csv
with open("desp.csv" , newline="") as csvfile:
    a = csv.reader(csvfile , delimiter=" " , quotechar="|")
    for i in a:
        print(",".join(i))
