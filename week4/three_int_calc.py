#capture three integer values from the user, add the first two numbers and divide by the third
#the program should also determne whether the result is great than zero

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

result = (num1 + num2) / num3
 
print(result)

#check to see if result is greater than zero
if result > 0:
    print(f"The mathematical operation is > 0")
else:
    print(f"The mathematical operation is <= 0") 



