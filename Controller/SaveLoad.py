import pickle

from Model.Dungeon import Dungeon
from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Maze import Maze


class SaveLoad:
    @staticmethod
    def save_game(data, name):
        data_file = open("LoadGame/"+name+".pickle", "wb")
        pickle.dump(data, data_file)
    @staticmethod
    def load_game(name):
        data_file = open("LoadGame/"+name+".pickle", "rb")
        data = pickle.load(data_file)
        return data
"""
Dungeon(False, ["tod", Element.AIR])
dungeon = Dungeon.pickle_dungeon()
SaveLoad.save_game(dungeon, "first")
print(Dungeon.get_instance())
print(Hero.get_instance())
print(Inventory.get_instance())
print(Maze.get_instance())
Dungeon.delete_instance()
print(Dungeon.get_instance())
print(Hero.get_instance())
print(Inventory.get_instance())
print(Maze.get_instance())
dungeon2 = SaveLoad.load_game("first")
dungeon_two = Dungeon(True, dungeon2[0], dungeon2[1], dungeon2[2])
print(Dungeon.get_instance())
print(Hero.get_instance())
print(Hero.get_instance().get_name())
print(Inventory.get_instance())
print(Maze.get_instance())
"""