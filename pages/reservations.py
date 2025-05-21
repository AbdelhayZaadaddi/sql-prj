import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import get_reservations

st.title("Liste des Réservations")

try:
    reservations = get_reservations()
    if reservations:
        st.write("Voici la liste des réservations :")
        
        df = pd.DataFrame(reservations, columns=["ID", "Client", "Date de début", "Date de fin", "Numéro de chambre"])
        st.dataframe(df)
    else:
        st.write("Aucune réservation trouvée.")
except Exception as e:
    st.error(f"Une erreur s'est produite lors de la récupération des réservations : {e}")