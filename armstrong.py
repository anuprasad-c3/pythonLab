num=int(input("Enter a number"))
num_str=str(num)
n=len(num_str)
armstrong=sum(int(digit)**n for digit in num_str)
if num== armstrong:
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT a Armstrong number")
