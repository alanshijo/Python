num1 = int(input("Enter the value of num1:"))
num2 = int(input("Enter the value of num2:"))
oper = input("Enter the operation you want to do:")
if oper == "+":
    print("num1+num2=", num1 + num2)
elif oper == "-":
    if num1 > num2:
        print("num1-num2=", num1 - num2)
    else:
        print("num1-num2=", num2 - num1)
elif oper == "*":
    print("num1*num2=", num1 * num2)
elif oper == "/":
    print("num1/num2 =", num1 / num2)
else:
    print("Invalid option.")
