import streamlit as st
from database import init_db

st.set_page_config(page_title="Hestion Hotel", layout="wide")  # Fixed typo
init_db()
st.title("Welcome to Hestion Hotel")
st.write("Bienvenue a Hestion Hotel")