words = input("Enter words separated by space :").split()

max_len = max(len(word) for word in words)

print("Length of the longest word :",max_len)
