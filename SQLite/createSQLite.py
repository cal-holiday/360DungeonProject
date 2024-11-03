import sqlite3
from Element import Element
con = sqlite3.connect("character.db")
cur = con.cursor()
cur.execute("CREATE TABLE monster(name, image, element, opposite, health, speed, basicAttack, specialAttack)")
data = [
    ('Earth Monster', 'earth_monster.png', Element.EARTH.value, Element.AIR.value, 50, 20, 5, 10),
    ('Fire Monster', 'fire_monster.png', Element.FIRE.value, Element.WATER.value, 30, 40, 5, 10),
    ('Air Monster', 'air_monster.png', Element.AIR.value, Element.EARTH.value, 20, 50, 5, 10),
    ('Water Monster', 'water_monster.png', Element.WATER.value, Element.FIRE.value, 40, 30, 5, 10)
]
cur.executemany("INSERT INTO monster VALUES(?, ?, ? ,?, ?, ?, ?, ?)", data)
con.commit()
