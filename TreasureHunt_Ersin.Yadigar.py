# Treasure Hunt Game
# Name: Ersin Yadigar

print("===================================")
print("       TREASURE HUNT GAME")
print("===================================")

player_name = input("Enter your name: ")

print("\nWelcome,", player_name + "!")
print("Your goal is to find the hidden treasure.")
print("Choose your path carefully and avoid the traps!")

print("\nYou arrive at a fork in the road.")
print("1. Take the path through the forest")
print("2. Take the path toward the river")

choice = input("Choose 1 or 2: ")

if choice == "1":
    print("\nYou enter the dark forest.")
    print("You hear strange sounds coming from behind the trees.")
    print("\n1. Follow the strange sounds")
    print("2. Follow an old stone path")

    forest_choice = input("Choose 1 or 2: ")

    if forest_choice == "1":
        print("\nA wild animal appears!")
        print("You run away and lose the treasure hunt.")

    elif forest_choice == "2":
        print("\nThe stone path leads you to an old wooden chest.")
        print("There are two keys beside the chest.")
        print("\n1. Use the silver key")
        print("2. Use the golden key")

        key_choice = input("Choose 1 or 2: ")

        if key_choice == "1":
            print("\nThe silver key does not fit.")
            print("The chest locks permanently.")
            print("The treasure remains hidden.")

        elif key_choice == "2":
            print("\nThe golden key opens the chest!")
            print("Congratulations,", player_name + "!")
            print("You found the hidden treasure!")

        else:
            print("\nInvalid choice.")
            print("The treasure remains hidden.")

    else:
        print("\nInvalid choice.")
        print("The treasure remains hidden.")

elif choice == "2":
    print("\nYou walk toward the river.")
    print("The water is moving fast, but you notice something across the river.")
    print("\n1. Swim across the river")
    print("2. Look for another way across")

    river_choice = input("Choose 1 or 2: ")

    if river_choice == "1":
        print("\nThe current is too strong.")
        print("You return to shore and the treasure hunt ends.")

    elif river_choice == "2":
        print("\nYou find an old wooden bridge.")
        print("After crossing it, you discover a mysterious cave.")
        print("\n1. Enter the cave")
        print("2. Walk around the cave")

        cave_choice = input("Choose 1 or 2: ")

        if cave_choice == "1":
            print("\nInside the cave, you find two tunnels.")
            print("1. Take the left tunnel")
            print("2. Take the right tunnel")

            tunnel_choice = input("Choose 1 or 2: ")

            if tunnel_choice == "1":
                print("\nThe tunnel ends at a dead end.")
                print("You leave the cave without finding the treasure.")

            elif tunnel_choice == "2":
                print("\nYou see something shining in the darkness.")
                print("Congratulations,", player_name + "!")
                print("You found the hidden treasure!")

            else:
                print("\nInvalid choice.")
                print("The treasure remains hidden.")

        elif cave_choice == "2":
            print("\nYou walk around the cave but find nothing.")
            print("The treasure hunt ends.")

        else:
            print("\nInvalid choice.")
            print("The treasure remains hidden.")

    else:
        print("\nInvalid choice.")
        print("The treasure remains hidden.")

else:
    print("\nInvalid choice. Please choose 1 or 2.")

print("\n===================================")
print("          GAME OVER")
print("===================================")