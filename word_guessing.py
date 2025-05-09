import random

word_bank = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi"]
word = random.choice(word_bank)

guessed_word = ["_"] * len(word)
attempts = len(word) + 2

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessed_word))

    guess = input("Enter a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        print("Try again! You have " + str(attempts) + " attempts left.")
        attempts -= 1
    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word: " + word)
        break
    else:
        print('\nYou\'ve run out of attempts! The word was: ' + word)