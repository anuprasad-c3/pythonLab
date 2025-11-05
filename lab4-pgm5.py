def add_numbers(*args):
    """This is a function """
    return sum(args)
nums = list(map(int,input("Enter numbers separated by space :").split()))
result = add_numbers(*nums)
print("Sum =",result)
print("\nFunction Docstring :\n",add_numbers.__doc__)
