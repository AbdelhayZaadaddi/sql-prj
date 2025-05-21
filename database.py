import sqlite3
import os

def init_db():
    if not os.path.exists("hotel.db"):
        connection = sqlite3.connect("hotel.db")
        c = connection.cursor()

        with open("db/schema.sql", "r", encoding="utf-8") as f:
            schema = f.read()
            c.executescript(schema)

        with open("db/data.sql", "r", encoding="utf-8") as f:
            data = f.read()
            c.executescript(data)

        connection.commit()
        connection.close()
        
        print("Base de données initialisée.")
    else:
        print("Base de données déjà existante.")
