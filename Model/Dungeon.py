from Model.CharacterFactory import CharacterFactory
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Maze import Maze


class Dungeon:
    __instance = None
    @staticmethod
    def get_instance():
        return Dungeon.__instance

    @staticmethod
    def delete_instance():
        Dungeon.__instance = None
        Hero.delete_instance()
        Inventory.delete_instance()
        Maze.delete_instance()

    def __init__(self, from_pickle, hero_info, maze_info=None, inventory_info=None):
        if not Dungeon.__instance is None:
            Dungeon.delete_instance()
        CharacterFactory.create_hero(hero_info[0], hero_info[1])
        Maze(6)
        Inventory()
        if from_pickle:
            Hero.get_instance().set_hp(hero_info[2])
            Hero.get_instance().set_x(hero_info[3])
            Hero.get_instance().set_y(hero_info[4])
            Maze.get_instance().set_array(maze_info[0])
            for item in inventory_info:
                Inventory.get_instance().add(item)
        Dungeon.__instance = self
    @staticmethod
    def pickle_dungeon():
        hero_info = [Hero.get_instance().get_name(), Hero.get_instance().get_element(), Hero.get_instance().get_hp(),
                     Hero.get_instance().get_x(), Hero.get_instance().get_y()]
        maze_info = [Maze.get_instance().get_array()]
        inventory_info = []
        for item in Inventory.get_instance().get_pillars():
            inventory_info.append(item)
        for item in Inventory.get_instance().get_vision_potions():
            inventory_info.append(item)
        for item in Inventory.get_instance().get_health_potions():
            inventory_info.append(item)
        return hero_info, maze_info, inventory_info