import json


class World:
    def __init__(self, id, hp, name):
        self.id = id
        self.hp = 1000
        self.name = name

    def damage(self, d):
        self.hp = self.hp - d

def create_new_world(world_name):
    print("create_new_world")
    id = 1
    hp = 1000
    name = world_name
    wc = World(1, 1000, world_name)
    return wc

def select_world():
    print("select_world")
    aw = create_new_world("rez")
    return aw

def save_world(aw):
    print("save_world")

    # convert object to dictionary
    world_dict = {}
    world_dict[aw.name] = aw.__dict__

    # convert dictionary to json
    world_json = json.dumps(world_dict)
    print (world_json)

    # write json to text file
    with open('GasparBorys/world_saves/' + aw.name + '.txt', 'w') as json_save:
       json.dump(world_json, json_save)

