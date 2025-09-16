num=int(input("Enter a number :"))
print(f"\n Multiplication Table of {num}")
print("-"*30)
for i in range(1,101):
    print(f"{num} x {i} = {num*i}")
