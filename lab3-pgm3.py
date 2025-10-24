n = int(input("Enter number of Elements :"))
my_list = []
for i in range(n):
    item = int(input("Enter items :"))
    my_list.append(item)
s = 0
for i in my_list:
    s += i
print("Sum of all items is :",s)
~                                
