word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print("Vowels in the word:", vowels)
