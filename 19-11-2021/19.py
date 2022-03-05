current = int(input("Enter the current year: "))
to = int(input("Enter the final year: "))
print("The leap years are:")
for year in range(current, to+1):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year)
        else:
            print(year)
