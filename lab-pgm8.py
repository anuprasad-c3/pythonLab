def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
n = int(input("Enter number of terms :"))
total = 0
for i in range(1,n+1):
    total +=(i**3)/factorial(i)
print("Sum of the series = ",total)
