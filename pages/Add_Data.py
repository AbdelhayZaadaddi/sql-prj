import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import insert_hotel, insert_reservation, insert_client, insert_prestation, insert_type_chambre, insert_chambre

st.title("Ajouter un Hôtel")
with st.form("add_hotel_form"):
    ville = st.text_input("Ville", max_chars=50)
    pays = st.text_input("Pays", max_chars=50)
    code_postal = st.number_input("Code Postal", min_value=0, step=1)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if ville and pays and code_postal:
            try:
                insert_hotel(ville, pays, code_postal)
                st.success(f"L'hôtel situé à {ville}, {pays} a été ajouté avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout de l'hôtel : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")


st.title("Ajouter un Reservation")
with st.form("add_reservation_form"):
    client_id = st.number_input("ID Client", min_value=1, step=1)
    date_debut = st.date_input("Date de Début")
    date_fin = st.date_input("Date de Fin")
    numero_chambre = st.number_input("Numéro de Chambre", min_value=1, step=1)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if client_id and date_debut and date_fin and numero_chambre:
            try:
                insert_reservation(client_id, date_debut, date_fin, numero_chambre)
                st.success(f"La réservation pour le client ID {client_id} a été ajoutée avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout de la réservation : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")


st.title("Ajouter un Client")
with st.form("add_client_form"):
    adresse = st.text_input("Adresse", max_chars=100)
    ville = st.text_input("Ville", max_chars=50)
    code_postal = st.number_input("Code Postal", min_value=0, step=1)
    email = st.text_input("Email", max_chars=100)
    telephone = st.text_input("Téléphone", max_chars=15)
    nom = st.text_input("Nom", max_chars=50)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if adresse and ville and code_postal and email and telephone and nom:
            try:
                insert_client(adresse, ville, code_postal, email, telephone, nom)
                st.success(f"Le client {nom} a été ajouté avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout du client : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")


st.title("Ajouter une Prestation")
with st.form("add_prestation_form"):
    prix = st.number_input("Prix", min_value=0.0, step=0.01)
    description = st.text_input("Description", max_chars=200)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if prix and description:
            try:
                insert_prestation(prix, description)
                st.success(f"La prestation '{description}' a été ajoutée avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout de la prestation : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")


st.title("Ajouter un Type de Chambre")
with st.form("add_type_chambre_form"):
    libelle = st.text_input("Libellé", max_chars=50)
    prix = st.number_input("Prix", min_value=0.0, step=0.01)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if libelle and prix:
            try:
                insert_type_chambre(libelle, prix)
                st.success(f"Le type de chambre '{libelle}' a été ajouté avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout du type de chambre : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")


st.title("Ajouter une Chambre")
with st.form("add_chambre_form"):
    numero = st.number_input("Numéro de Chambre", min_value=1, step=1)
    type_chambre_id = st.number_input("ID Type de Chambre", min_value=1, step=1)

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if numero and type_chambre_id:
            try:
                insert_chambre(numero, type_chambre_id)
                st.success(f"La chambre numéro {numero} a été ajoutée avec succès.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de l'ajout de la chambre : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")

