import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import get_clients


st.title("Liste des Clients")

clients = get_clients()

if clients:
    st.write("Voici la liste des clients :")
    
    df = pd.DataFrame(clients, columns=["ID", "Nom", "Adresse", "Ville", "Code Postal", "Email", "Téléphone"])
    
    st.dataframe(df)
else:
    st.write("Aucun client trouvé.")

