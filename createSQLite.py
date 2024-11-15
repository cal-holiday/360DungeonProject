import sqlite3
from Element import Element
con = sqlite3.connect("character.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS monster(name, image, element UNIQUE, max_health, agility)")
data = [
    ('Earth Monster', 'earth_monster.png', Element.EARTH.value, 50, 4),
    ('Air Monster', 'air_monster.png', Element.AIR.value, 20, 16),
    ('Water Monster', 'water_monster.png', Element.WATER.value, 30, 8),
    ('Fire Monster', 'fire_monster.png', Element.FIRE.value, 40, 12),
]
cur.executemany("INSERT INTO monster VALUES(?, ?, ? ,?, ?)", data)
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS hero(image, element UNIQUE, max_health, agility)")
data = [
    ('earth_hero.png', Element.EARTH.value, 100, 4),
    ('air_hero.png', Element.AIR.value, 40, 16),
    ('water_hero.png', Element.WATER.value, 60, 8),
    ('fire_hero.png', Element.FIRE.value, 80, 12),
]
cur.executemany("INSERT INTO hero VALUES(?, ?, ?, ?)", data)
con.commit()
con.close()