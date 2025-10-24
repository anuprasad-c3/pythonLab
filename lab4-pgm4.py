start = int(input("Enter start of range :"))
end = int(input("Enter end of range :"))
result = []
for num in range(start,end+1):
    if 1000 <= num <= 9999:
        if(int(num**0.5))**2==num:
            digits = str(num)
            if all (int(d)%2==0 for d in digits):
                result.append(num)

print("4 digit perfect square will all even digit :")
print(result)
