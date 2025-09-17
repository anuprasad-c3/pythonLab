num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

add=num1+num2
sub=num1-num2
mul=num1*num2

if num2 != 0:
    div = num1 / num2
    mod = num1 % num2
else:
    div = "Not defined"
    mod = "Undefined"

print("Addition of ",num1,"and",num2,"is ",add)
print("Subtraction of ",num1,"and",num2,"is ",sub)
print("Multiplication of ",num1,"and",num2,"is ",mul)
print("Division of ",num1,"and",num2,"is ",div)
print("Modules of ",num1,"and",num2,"is ",mod)


