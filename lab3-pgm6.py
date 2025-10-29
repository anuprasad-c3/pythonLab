N = int(input("Enter number of steps :"))
for i in range(1,N+1):
    for j in range(1,i+i):
        print(i*j,end = " ")
    print()
