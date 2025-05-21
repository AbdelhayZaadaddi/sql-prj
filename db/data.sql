INSERT INTO Hotel(id, ville, pays, code_postal) VALUES
(1, 'Paris', 'France', 75001),
(2, 'Londres', 'Royaume-Uni', 10001),
(3, 'New York', 'États-Unis', 10001),
(4, 'Tokyo', 'Japon', 10001),
(5, 'Berlin', 'Allemagne', 10001);

INSERT INTO Client(id, adresse, ville, code_postal, email, telephone, nom) VALUES
(1, '10 Rue de Paris', 'Paris', 75001, 'client1@example.com', '0123456789', 'Jean Dupont'),
(2, '221B Baker Street', 'Londres', 10001, 'client2@example.com', '9876543210', 'Sherlock Holmes'),
(3, '5th Avenue', 'New York', 10001, 'client3@example.com', '1234567890', 'John Doe'),
(4, 'Shibuya', 'Tokyo', 10001, 'client4@example.com', '0987654321', 'Hiro Tanaka'),
(5, 'Alexanderplatz', 'Berlin', 10001, 'client5@example.com', '5678901234', 'Hans Müller');

INSERT INTO Prestation(id, prix, description) VALUES
(1, 50.00, 'Petit déjeuner'),
(2, 100.00, 'Déjeuner'),
(3, 150.00, 'Dîner'),
(4, 200.00, 'Spa'),
(5, 300.00, 'Excursion');

INSERT INTO TypeChambre(id, libelle, prix) VALUES
(1, 'Simple', 100.00),
(2, 'Double', 150.00),
(3, 'Suite', 300.00),
(4, 'Deluxe', 500.00),
(5, 'Penthouse', 1000.00);

INSERT INTO Chambre(id, numero, etage, balcon, type_id, hotel_id) VALUES
(1, 101, 1, TRUE, 1, 1),
(2, 102, 1, FALSE, 2, 1),
(3, 201, 2, TRUE, 3, 2),
(4, 202, 2, FALSE, 4, 2),
(5, 301, 3, TRUE, 5, 3);

INSERT INTO Reservation(id, date_debut, date_fin, client_id, Chambre_id) VALUES
(1, '2025-06-01', '2025-06-05', 1, 1),
(2, '2025-06-10', '2025-06-15', 2, 2),
(3, '2025-07-01', '2025-07-07', 3, 3),
(4, '2025-07-15', '2025-07-20', 4, 4),
(5, '2025-08-01', '2025-08-10', 5, 5);