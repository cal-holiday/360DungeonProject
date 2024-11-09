import sqlite3
from Element import Element
from Monster import Monster
from Hero import Hero
class CharacterFactory:

    @staticmethod
    def createMonster(element):
        element_val = element.value
        con = sqlite3.connect("character.db")
        cur = con.cursor()
        name = cur.execute("SELECT name FROM monster WHERE element=element_val")
        image = cur.execute("SELECT image FROM monster WHERE element=element_val")
        max_hp = cur.execute("SELECT health FROM monster WHERE element=element_val")
        agility = cur.execute("SELECT agility FROM monster WHERE element=element_val")
        element = element
        opposite = Element(cur.execute("SELECT opposite FROM monster WHERE element=element_val"))
        con.close()
        return Monster(name, image, max_hp, agility, element, opposite)

    def createHero(self, name, element):
        element_val = element.value
        con = sqlite3.connect("character.db")
        cur = con.cursor()
        image = cur.execute("SELECT image FROM hero WHERE element=element_val")
        max_hp = cur.execute("SELECT health FROM hero WHERE element=element_val")
        agility = cur.execute("SELECT agility FROM hero WHERE element=element_val")
        element = element
        opposite = Element(cur.execute("SELECT opposite FROM hero WHERE element=element_val"))
        con.close()
        return Hero(name, image, max_hp, agility, element, opposite)