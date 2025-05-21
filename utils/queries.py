import sqlite3

def get_connection():
    return sqlite3.connect("hotel.db")

def get_hotels():
    connection = get_connection()
    c = connection.cursor()
    c.execute("SELECT * FROM Hotel")
    hotels = c.fetchall()
    connection.close()
    return hotels

def insert_hotel(id, ville, pays, code_postal):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO Hotel (id, ville, pays, code_postal) VALUES (?, ?, ?, ?)", (id, ville, pays, code_postal))
    connection.commit()
    connection.close()

def get_clients():
    connection = get_connection()
    c = connection.cursor()
    c.execute("SELECT * FROM Client")
    clients = c.fetchall()
    connection.close()
    return clients

def insert_client(adresse, ville, code_postal, email, telephone, nom):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO Client (adresse, ville, code_postal, email, telephone, nom) VALUES (?, ?, ?, ?, ?, ?)", 
              (adresse, ville, code_postal, email, telephone, nom))
    connection.commit()
    connection.close()

def get_prestations():
    connection = get_connection()
    c = connection.cursor()
    c.execute("SELECT * FROM Prestation")
    prestations = c.fetchall()
    connection.close()
    return prestations

def insert_prestation(prix, description):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO Prestation (prix, description) VALUES (?, ?)", (prix, description))
    connection.commit()
    connection.close()

def get_type_chambres():
    connection = get_connection()
    c = connection.cursor()
    c.execute("SELECT * FROM TypeChambre")
    type_chambres = c.fetchall()
    connection.close()
    return type_chambres

def insert_type_chambre(libelle, prix):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO TypeChambre (libelle, prix) VALUES (?, ?)", (libelle, prix))
    connection.commit()
    connection.close()

def get_chambres():
    connection = get_connection()
    c = connection.cursor()
    c.execute("SELECT * FROM Chambre")
    chambres = c.fetchall()
    connection.close()
    return chambres

def insert_chambre(numero, etage, balcon, type_id, hotel_id):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO Chambre (numero, etage, balcon, type_id, hotel_id) VALUES (?, ?, ?, ?, ?)", 
              (numero, etage, balcon, type_id, hotel_id))
    connection.commit()
    connection.close()

def get_reservations():
    connection = get_connection()
    c = connection.cursor()
    c.execute("""
        SELECT r.id, c.nom, r.date_debut, r.date_fin, ch.numero
        FROM Reservation r
        JOIN Client c ON r.client_id = c.id
        JOIN Chambre ch ON r.Chambre_id = ch.id
    """)
    reservations = c.fetchall()
    connection.close()
    return reservations

def insert_reservation(date_debut, date_fin, client_id, chambre_id):
    connection = get_connection()
    c = connection.cursor()
    c.execute("INSERT INTO Reservation (date_debut, date_fin, client_id, Chambre_id) VALUES (?, ?, ?, ?)", 
              (date_debut, date_fin, client_id, chambre_id))
    connection.commit()
    connection.close()