import sqlite3
from Element import Element
from Monster import Monster
class MonsterFactory():

    def createMonster(theSelf, theElement):
        element_val = theElement.value
        con = sqlite3.connect("character.db")
        cur = con.cursor()
        name = cur.execute("SELECT name FROM monster WHERE element=element_val")
        image = cur.execute("SELECT image FROM monster WHERE element=element_val")
        health = cur.execute("SELECT health FROM monster WHERE element=element_val")
        max_hp = health
        agility = cur.execute("SELECT agility FROM monster WHERE element=element_val")
        element = theElement
        opposite = Element(cur.execute("SELECT opposite FROM monster WHERE element=element_val"))
        basic_attack = cur.execute("SELECT basicAttack FROM monster WHERE element=element_val")
        special_attack = cur.execute("SELECT specialAttack FROM monster WHERE element=element_val")
        con.close()
        return Monster(name, image, health, max_hp, agility, element, opposite, basic_attack, special_attack)