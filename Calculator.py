
# Build a Simple Calculator

print("Select an Operation to Perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")


operation = int(input("Select an Operation:"))

if operation == 1:
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))
  print("The Sum is num1 and num2",str(num1+num2))

elif operation == 2:
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))
  print("The Subtraction is num1 and num2:"+str(num1-num2))


elif operation == 3:
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))
  print("The Multiplication is:"+str(num1*num2))


elif operation == 4:
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))
  print("The Divide  is:"+str(num1/num2))


else:
    print("Invalid entry")

