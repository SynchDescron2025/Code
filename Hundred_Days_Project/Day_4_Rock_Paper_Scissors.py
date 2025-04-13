import random
print("Welcome to Rock Paper Scissors Game")
print("Hit n to exit the program")
my_list = ["rock","paper","scissors"]

choice = int(input("Type 1 for rock,2 for paper,3 for scissors"))
random_choice = random.choice(my_list)
print("Computer choose "+ random_choice)


if choice == 1:
    if random_choice == "rock":
        print("It's a Draw!")
    elif random_choice == "paper":
        print("Computer Won")
    elif random_choice == "scissors":
        print("You Won")
elif choice == 2:
    if random_choice == "rock":
        print("You Won!")
    elif random_choice == "paper":
        print("It's a Draw!")
    elif random_choice == "scissors":
        print("Computer Won!")
elif choice == 3:
    if random_choice == "rock":
        print("Computer Won!")
    elif random_choice == "paper":
        print("You Won!")
    elif random_choice == "scissors":
        print("It's a Draw!")
        
        
