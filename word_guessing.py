import random

word_bank = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi"]
word = random.choice(word_bank)

guessed_word = ["_"] * len(word)
attempts = len(word) + 2

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessed_word))