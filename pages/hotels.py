import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import get_hotels

st.title("Liste des Hôtels")
hotels = get_hotels()
if hotels:
    st.write("Voici la liste des hôtels :")
    
    df = pd.DataFrame(hotels, columns=["ID", "Ville", "Pays", "Code Postal"])
    
    st.dataframe(df)
else: 
    st.write("Aucun hôtel trouvé.")