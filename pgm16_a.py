numbers = input("Enter integers separated by commas: ")
num_list = [int(x) for x in numbers.split(",")]
positive = [num for num in num_list if num > 0]
print("Positive numbers:", positive)
