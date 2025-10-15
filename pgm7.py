text = input("Enter a line of text :")

words = text.split()

count = {}

for word in words:
    count[word] = count.get(word,0)+1
print("Output :",count)    
