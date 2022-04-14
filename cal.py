# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide

print("Select an operation to perform:")
print("1.Add")
print("2.Subtract")
print("3.Mulitiply")
print("4. Divide")

operation = input()

# code for Addition

if operation =="1":
    
    num1 = int(input("Enter first number:"))
    num2 =int(input("Enter second number:"))
    print(num1 + num2)

    #code for subtraction

elif operation=="2":

    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(num1 - num2)

    #code for multiplication

elif operation=="3":

    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(num1 * num2)


    #code for division

elif operation =="4":

    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(num1 / num2)

else:
    print("Invalid Entry")
