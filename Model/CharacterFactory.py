import sqlite3
from Model.Monster import Monster
from Model.Hero import Hero

class CharacterFactory:
    @staticmethod
    def create_monster(element):
        element_val = element.value
        con = sqlite3.connect("../Controller/character.db")
        cur = con.cursor()
        sql_query = f"SELECT name, image, max_health, agility FROM monster WHERE element = {element_val}"
        cur.execute(sql_query)
        result = cur.fetchone()
        if result:
            name, image, max_hp, agility = result
            element = element
            con.close()
            return Monster(name, image, max_hp, agility, element)
        else:
            con.close()
            raise ValueError(f"No monster found for element {element_val}")

    @staticmethod
    def create_hero(name, element):
        element_val = element.value
        con = sqlite3.connect("../Controller/character.db")
        cur = con.cursor()
        sql_query = f"SELECT image, max_health, agility FROM hero WHERE element = {element_val}"
        cur.execute(sql_query)
        result = cur.fetchone()
        if result:
            image, max_hp, agility = result
            element = element
            con.close()
            return Hero(name, image, max_hp, agility, element)
        else:
            con.close()
            raise ValueError(f"No hero found for element {element_val}")
