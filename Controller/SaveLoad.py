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
