import csv
with open("desp.csv" , newline="") as csvfile:
    a = csv.DictReader(csvfile)
    print("Period   Data_value    Subject")
    print("--------------------------------------")
    for i in a:
        print(i["Period"] , "|" , i["Data_value"] , "|" , i["Subject"])
