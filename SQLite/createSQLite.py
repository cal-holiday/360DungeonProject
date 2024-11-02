import sqlite3
con = sqlite3.connect("character.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE monster(name, image,element, opposite, health, 
    speed, basicAttack, specialAttack""")
cur.execute("""
    INSERT INTO monster VALUES
        ()
        ()
        ()
        ()
    """)