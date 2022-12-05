from creatures import *

import json



class Character(Creature):

    def damage(self, d):
        self.hp = self.hp - d

    def heal(self, h):
        self.hp = self.hp + h

    def add_to_character_index(self):
        print("add to character index")

    def move_east(self):
        print("move_east")
        self.coords[0] = self.coords[0] + 1

    def move_west(self):
        print("move_west")
        self.coords[0] = self.coords[0] - 1

    def move_north(self):
        print("move_north")
        self.coords[1] = self.coords[1] + 1

    def move_south(self):
        print("move_south")
        self.coords[1] = self.coords[1] - 1

def select_character():
    print("select_character")
    ac = create_new_character("jom")
    return ac

def create_new_character(character_name):
    print("create_new_character")
    
    hp = 100
    luck = 25
    knowledge = 1.0
    coords = [0,0,0,0,0] 
    nc = Character(1, character_name, hp, luck, knowledge, coords)
    return nc
    

def random_character_generator():
    print("random_character_generator")

def save_character(ac):
    print("save_character")

    # convert object to dictionary
    character_dict = {}
    character_dict[ac.name] = ac.__dict__

    # convert dictionary to json
    character_json = json.dumps(character_dict)
    print (character_json)

    # write json to text file
    with open('GasparBorys/character_saves/' + ac.name + '.txt', 'w') as json_save:
       json.dump(character_json, json_save)


# ------------------------







