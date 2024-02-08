# create a list of words then using list comprehension print words with odd number of characters
words = ["Forest", "Hills", "Mountain", "Park","Snake"]
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(odd_length_words)
