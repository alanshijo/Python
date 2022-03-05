signal = str(input("Enter the colour of the signal:"))
if signal == "red" or signal == "RED":
    print("STOP")
elif signal == "green" or signal == "GREEN":
    print("GO")
elif signal == "orange" or signal == "ORANGE":
    print("BE SLOW")
else:
    print("Invalid option")
