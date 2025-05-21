import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import get_prestations

st.title("Liste des Prestations")
prestations = get_prestations()
if prestations:
    st.write("Voici la liste des prestations :")
    
    df = pd.DataFrame(prestations, columns=["ID", "Nom", "Prix"])
    
    st.dataframe(df)
else:
    st.write("Aucune prestation trouvée.")