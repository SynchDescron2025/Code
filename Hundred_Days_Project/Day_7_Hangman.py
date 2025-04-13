import requests
import random
print("Welcome to Hangman Game")

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)

words = [word.decode('utf-8') for word in response.content.splitlines()]
filtered_words = [word for word in words if len(word) == 6]

random_word = random.choice(filtered_words)
empty_word = ["_"] * 6
word =list(random_word)
life = 6

while life >0:
    choice = input("Enter a character").lower()
    if choice in word:
        for idx, letter in enumerate(word):
            if letter == choice:
                empty_word[idx] = choice
        print("Correct " , " ".join(empty_word))
    else:
        life -= 1
        print(f"Wrong!, you have {life}'s left!")
        print("".join(empty_word))
    if "_" not in empty_word:
        print("🎉 Congratulations! You guessed the word:", random_word)
        break
if "_" in empty_word:
    print("💀 Game Over! The word was:", random_word)










