from text import *
from game import *



def main_game_menu():
    print("main_game_menu")

    while True:
        user_input = input(default_prompt)
        print(" * user_input = ", user_input)

        if user_input == "p":
            play_game()

        elif user_input == "h":
            print(main_game_menu_list)

        elif user_input == "q":
            quit_game()

        else:
            print("That is not a valid command :( ")



