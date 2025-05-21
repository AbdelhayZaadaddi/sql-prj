import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.queries import get_chambres

st.title("Liste des Chambres")
chambres = get_chambres()

if chambres:
    st.write("Voici la liste des chambres :")
    
    df = pd.DataFrame(chambres, columns=["ID", "Type de chambre", "Prix", "Numéro", "Étage", "Balcon"])
    
    st.dataframe(df)
else:
    st.write("Aucune chambre trouvée.")