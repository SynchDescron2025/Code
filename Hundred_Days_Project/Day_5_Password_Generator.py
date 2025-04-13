import random
print("Welcome to Password Generator")

letters = []
symbols = []
numbers = []
for i in range(65,91):
    letters.append(chr(i))
for i in range(97,123):
    letters.append(chr(i))
for i in range(33,48):
    symbols.append(chr(i))
for i in range(48,58):
    numbers.append(chr(i))

choice_letters = int(input("How many letters do you want in your password?"))
choice_symbols= int(input("How many symbols do you want in your password?"))
choice_numbers = int(input("How many numbers do you want in your password?"))

password = []
for i in range(0, choice_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)

for i in range(0, choice_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

for i in range(0, choice_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)

random.shuffle(password)
new_password = ''.join(password)
print("Your password is:" + new_password)



