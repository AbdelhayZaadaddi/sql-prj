import sqlite3

def init_db():
    connection = sqlite3.connect("hotel.db")
    c = connection.cursor()

    with open("db/shema.sql") as sql_f:
        sql_sqript = sql_f.read()

    
    c.executescript(sql_sqript)

    connection.commit()
    connection.close()
    print("Database initialized successfully.")