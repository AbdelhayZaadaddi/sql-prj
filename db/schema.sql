CREATE TABLE IF NOT EXISTS Hotel(
    id INT PRIMARY KEY,
    ville VARCHAR(50),
    pays VARCHAR(50),
    code_postal INT
);

CREATE TABLE IF NOT EXISTS Client(
    id INT PRIMARY KEY,
    adresse VARCHAR(100),
    ville VARCHAR(50),
    code_postal INT,
    email VARCHAR(100),
    telephone VARCHAR(15),
    nom VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Prestation(
    id INT PRIMARY KEY,
    prix DECIMAL(10, 2),
    description VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS TypeChambre(
    id INT PRIMARY KEY,
    libelle VARCHAR(50),
    prix DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS Chambre(
    id INT PRIMARY KEY,
    numero INT,
    etage INT,
    balcon BOOLEAN,
    type_id INT,
    hotel_id INT,
    FOREIGN KEY (type_id) REFERENCES TypeChambre(id),
    FOREIGN KEY (hotel_id) REFERENCES Hotel(id)
);

CREATE TABLE IF NOT EXISTS Reservation(
    id INT PRIMARY KEY,
    date_debut DATE,
    date_fin DATE,
    client_id INT,
    Chambre_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(id),
    FOREIGN KEY (Chambre_id) REFERENCES Chambre(id)
);