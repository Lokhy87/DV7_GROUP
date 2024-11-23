import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import base64

# Cargar la imagen desde el archivo subido
image_path = r"C:\Users\admin\OneDrive\Documentos\GitHub\DV7_GROUP\imagenes\portada.jpg"
image = Image.open(image_path)

# Codificar la imagen a base64 para insertarla en HTML
with open(image_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()

# CSS para fondo negro y estilo
st.markdown("""
    <style>
        .stApp {
            background-color: black;
        }

        .title-overlay {
            position: relative;
            text-align: center;
            color: white;
            font-weight: bold;
        }

        .background-image {
            width: 100%;
            height: 100%;
            filter: blur(3px); /* Nivel de difuminado */
            opacity: 0.8; /* Transparencia */
            object-fit: cover; /* Asegura que cubra todo el contenedor */
        }

        .title-overlay h1 {
            position: absolute;
            top: 50%; /* Centrar verticalmente */
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 48px; /* Tamaño del título */
            text-shadow: 2px 2px 5px rgba(0,0,0,0.8); /* Sombra para resaltar texto */
            color: #ffffff; /* Color blanco */
        }
    </style>
""", unsafe_allow_html=True)

# Mostrar la imagen con título sobre ella
st.markdown(f"""
    <div class="title-overlay">
        <img class="background-image" src="data:image/png;base64,{img_base64}" />
        <h1>LaLiga y LaLiga2 - Base de Datos</h1>
    </div>
""", unsafe_allow_html=True)

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

# Subtítulo para la selección del rango de edad
st.markdown(f"""
    <div class="box">
        <h3>Seleccionar un rango de edad:</h3>
    </div>
""", unsafe_allow_html=True)
# st.subheader('Seleccionar un rango de edad:')
rango_edad = st.slider('Selecciona el rango de edad:', min_value=18, max_value=40, value=(18, 35), step=1)





# Subtitulo para la seleccion de Valor Mercado
st.markdown("""
    <div class="box">
        <h3 style="color: red;">Selecciona un rango de Valor Mercado:</h3>
""", unsafe_allow_html=True)

#st.subheader('Selecciona un rango de Valor Mercado:')
valor_mercado_min = int(df['Valor Mercado'].min())
valor_mercado_max = int(df['Valor Mercado'].max())
rango_valor_mercado = st.slider('Selecciona el rango de Valor Mercado:',
                                min_value=valor_mercado_min,
                                max_value=valor_mercado_max,
                                value=(valor_mercado_min, valor_mercado_max),
                                step=100000)


