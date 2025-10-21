<<<<<<< HEAD
word = input("Enter a string word :")
if len(word)<3:
=======
word = input("Enter a word: ")

if len(word) < 3:
>>>>>>> f423e34fdf945fa752e4e43b87ef28aed6ab753a
    result = word
elif word.endswith("ing"):
    result = word + "ly"
else:
    result = word + "ing"
<<<<<<< HEAD
print("Modified word :",result)
=======

print("Modified word:", result)
>>>>>>> f423e34fdf945fa752e4e43b87ef28aed6ab753a
