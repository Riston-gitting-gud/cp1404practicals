"""
Word Occurrences
Estimate: 1 hour 10 minutes
Actual: 48 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")


