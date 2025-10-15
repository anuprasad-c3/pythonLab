user_input = input("Enter first names separated by commas: ")

names = [name.strip() for name in user_input.split(",")]

count = sum(name.lower().count('a') for name in names)

print(f"Total occurrences of 'a': {count}")
