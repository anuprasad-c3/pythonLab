list1 = list(map(int,input("Enter the first list of integers(separated by space): ").split()))
list2 = list(map(int,input("Enter the Second list of integers(separated by space): ").split()))

same_len = len(list1) == len(list2)
print(f"lists are of the same length :{same_len}")

same_sum = sum(list1) == sum(list2)
print(f"Lists sum to the same value :{same_sum}")

common_values = set(list1) & set(list2)
if common_values:
    print(f"Common values found in both lists :{common_values}")
else:
    print(f"No common values found in both list.")
