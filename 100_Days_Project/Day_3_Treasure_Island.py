print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

choice_1 = input("You are at a crossroad, where do you want to go?Left or Right?").lower()

if choice_1 == "left":
    choice_2 = input("You have come to a lake.There is an island in the middle of the lake.Swim or Wait?").lower()
    if choice_2 == "wait":
        choice_3 = input(("You arrive at the island.There is house with 3 doors.One Red,One Blue, One Yellow.Which one do you choose?Red or Blue or Yellow?")).lower()
        if choice_3 == "red":
            print("It's a room full of fire.Game Over")
        elif choice_3 == "blue":
            print("You enter a room full of beasts.Game Over")
        elif choice_3 == "yellow":
            print("You have found the treasure.You Win") 
        else:
            print("Game Over")       
    else:
        print("Attacked by trout.Game Over")

else:
    print("You have fell into a hole.Game Over")