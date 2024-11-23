import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# STREAMLIT

# Personalización de CSS
st.markdown("""
    <style>
        .title {
            color: white;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background-image: url('C:/Users/abolt/Documents/GitHub/DV7_GROUP/imagenes/portada.jpg');
            background-size: cover;
            background-position: center;
            padding: 50px 0; /* Espaciado superior e inferior */
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.markdown('<p class="title">LaLiga y LaLiga2 - Base de Datos</p>', unsafe_allow_html=True)

# Cargar el archivo CSV y mostrar un mensaje de error si no se puede cargar
try:
    df = pd.read_csv('DB_Jugadores_columnasUtiles.csv')
    #st.write("Datos cargados correctamente.")
except Exception as e:
    st.error(f"No se pudo cargar el archivo CSV. Error: {e}")

# Verificar las primeras filas del DataFrame para conocer la estructura
if not df.empty:
    st.write("Vista previa de los datos:")
    st.dataframe(df.head())

# Subtítulo para la selección de liga
st.subheader('Selecciona una Liga:')
ligas = ['LaLiga', '2ª División']
liga_seleccionada = st.selectbox('Elige una liga:', ligas)