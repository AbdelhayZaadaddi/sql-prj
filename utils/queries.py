import sqlite3

print("✅ utils.queries loaded")


def get_connection():
    return sqlite3.connect("hotel.db")


def get_reservations():
    connection = get_connection()
    c = connection.cursor()

    c.execute("""
        SELECT r.id, c.nom, r.date_debut, r.date_fin
        FROM Reservation r
        JOIN Client c ON r.client_id = c.id
    """)

    reservations = c.fetchall()
    connection.close()
    return reservations


def get_clients():
    connection = get_connection()
    c = connection.cursor()

    c.execute("""SELECT id, nom, adresse, ville, code_postal, email, telephone
    FROM Client""")
    clients = c.fetchall()
    connection.close()
    return clients


def get_chambres():


def get_prestations():

def get_hotel():
    