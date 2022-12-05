from text import *
from world import *
from character import *



def start_game():
    print (splash_prompt)

def run_game(ac, aw):
    print(ac.name, "and", aw.name)
    print(aw)
    while True:
        user_input = input("enter action: ")

        if user_input == "e":
            ac.move_east()
            print(ac.coords)

        elif user_input == "w":
            ac.move_west()
            print(ac.coords)

        elif user_input == "n":
            ac.move_north()
            print(ac.coords)

        elif user_input == "s":
            ac.move_south()
            print(ac.coords)

        elif user_input == "cs":
            character_stats = ac.__dict__
            for i in character_stats:
                print(i, character_stats[i])

        elif user_input == "ws":
            world_stats = aw.__dict__
            for i in world_stats:
                print(i, world_stats[i])

        elif user_input == "sw":
            save_world(aw)

        elif user_input == "sc":
            save_character(ac)

        elif user_input == "q":
            break

        else:
            print(not_a_valid_command)


def play_game():
    print("play_game")

    ac = select_character()
    aw = select_world()
    run_game(ac, aw)

def quit_game():
    print(quit_prompt)
    quit()





