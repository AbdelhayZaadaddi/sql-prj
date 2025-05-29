# Gestion Hôtel

## Description
Ce projet est une application de gestion d'hôtel développée avec Python et Streamlit. Elle permet de gérer les hôtels, les clients, les chambres, les prestations, et les réservations. Les données sont stockées dans une base SQLite.

## Fonctionnalités
- Afficher la liste des hôtels, clients, chambres, prestations, et réservations.
- Ajouter des hôtels, clients, chambres, prestations, et réservations.
- Base de données SQLite avec schéma et données initiales.

## Structure du projet
Collecting workspace information```markdown
# Gestion Hôtel

## Description
Ce projet est une application de gestion d'hôtel développée avec Python et Streamlit. Elle permet de gérer les hôtels, les clients, les chambres, les prestations, et les réservations. Les données sont stockées dans une base SQLite.

## Fonctionnalités
- Afficher la liste des hôtels, clients, chambres, prestations, et réservations.
- Ajouter des hôtels, clients, chambres, prestations, et réservations.
- Base de données SQLite avec schéma et données initiales.

## Structure du projet
```
├── app.py                # Point d'entrée de l'application Streamlit
├── database.py           # Initialisation de la base de données
├── db/
│   ├── schema.sql        # Schéma de la base de données
│   ├── data.sql          # Données initiales
├── pages/                # Pages Streamlit
│   ├── Add_Data.py       # Page pour ajouter des données
│   ├── chambres.py       # Page pour afficher les chambres
│   ├── clients.py        # Page pour afficher les clients
│   ├── hotels.py         # Page pour afficher les hôtels
│   ├── Prestation.py     # Page pour afficher les prestations
│   ├── reservations.py   # Page pour afficher les réservations
├── utils/
│   ├── queries.py        # Fonctions pour interagir avec la base de données
│   ├── __init__.py       # Fichier d'initialisation du module utils
├── hotel.db              # Base de données SQLite (générée automatiquement)
├── README.md             # Documentation du projet
└── .gitignore            # Fichiers ignorés par Git
```

## Prérequis
- Python 3.12 ou version ultérieure
- Streamlit
- SQLite

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/AbdelhayZaadaddi/sql-prj
   cd sql-prj
   ```
2. Installez les dépendances :
   ```bash
   pip install streamlit pandas
   ```

## Utilisation
1. Initialisez la base de données :
   - La base de données est automatiquement initialisée lors du lancement de l'application.
2. Lancez l'application :
   ```bash
   streamlit run app.py
   ```
3. Accédez à l'application via votre navigateur à l'adresse indiquée par Streamlit.

## Auteur
Ce projet a été développé par 
`Abdelhay Zaadaddi`,
`Ilyass Youness`
