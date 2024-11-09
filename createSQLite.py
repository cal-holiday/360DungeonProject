import sqlite3
from Element import Element
con = sqlite3.connect("character.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS monster(name, image, element UNIQUE, opposite, max_health, agility, basic_attack, special_attack)")
data = [
    ('Earth Monster', 'earth_monster.png', Element.EARTH.value, Element.AIR.value, 50, 4, 5, 10),
    ('Air Monster', 'air_monster.png', Element.AIR.value, Element.EARTH.value, 20, 16, 5, 10),
    ('Water Monster', 'water_monster.png', Element.WATER.value, Element.FIRE.value, 30, 8, 5, 10),
    ('Fire Monster', 'fire_monster.png', Element.FIRE.value, Element.WATER.value, 40, 12, 5, 10),
]
cur.executemany("INSERT INTO monster VALUES(?, ?, ? ,?, ?, ?, ?, ?)", data)
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS hero(image, element UNIQUE, opposite, max_health, agility, basic_attack, special_attack)")
data = [
    ('earth_hero.png', Element.EARTH.value, Element.AIR.value, 100, 4, 5, 10),
    ('air_hero.png', Element.AIR.value, Element.EARTH.value, 40, 16, 5, 10),
    ('water_hero.png', Element.WATER.value, Element.FIRE.value, 60, 8, 5, 10),
    ('fire_hero.png', Element.FIRE.value, Element.WATER.value, 80, 12, 5, 10),
]
cur.executemany("INSERT INTO hero VALUES(?, ?, ? ,?, ?, ?, ?, ?)", data)
con.commit()
con.close()