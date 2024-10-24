import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# STREAMLIT

# Título de la aplicación
#st.header('LaLiga y LaLiga2 - Base de datos')

# Cargar la imagen usando st.image para asegurar que se muestre correctamente
image = Image.open('C:\\Users\\abolt\\Documents\\GitHub\\DS_Online_Feb24\\DV7_GROUP\\imagenes\\portada.jpg')

# Mostrar imagen con st.image
st.image(image, use_column_width=True)
st.markdown(
    """
    <style>
    .container {
        position: relative;
        width: 100%;
        height: 300px;
        background-image: url('C:\\Users\\abolt\\Documents\\GitHub\\DS_Online_Feb24\\DV7_GROUP\\imagenes\\portada.jpg');
        background-size: cover;
        background-position: center;
        text-align: center;
        color: white;
    }
    .title {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 2.5em;
        font-weight: bold;
        background-color: rgba(0, 0, 0, 0.5); /* Fondo oscuro semi-transparente detrás del texto */
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    <div class="container">
        <div class="title">LaLiga y LaLiga2 - Base de datos</div>
    </div>
    """,
    unsafe_allow_html=True)

# Cargar el archivo CSV y mostrar un mensaje de error si no se puede cargar
try:
    df = pd.read_csv('DB_Jugadores_1a_2da_Division.csv')
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

# Subtítulo para la selección del rango de edad
st.subheader('Seleccionar un rango de edad:')
rango_edad = st.slider('Selecciona el rango de edad:', min_value=18, max_value=40, value=(18, 35), step=1)

# Subtítulo para la selección de posición
st.subheader('Selecciona una posición:')
posiciones = [
    'Defensa central',
    'Mediocentro',
    'Delantero centro',
    'Portero',
    'Extremo derecho',
    'Extremo izquierdo',
    'Lateral derecho',
    'Lateral izquierdo',
    'Pivote',
    'Mediocentro ofensivo',
    'Mediapunta',
    'Interior derecho',
    'Interior izquierdo'
]
posicion_seleccionada = st.selectbox('Elige una posición:', posiciones)

# Seleccion proveedor 
st.subheader('Selecciona un proveedor:')
proveedor = [
    'Proveedor no encontrado',
    'Nike',
    'adidas',
    'Puma',
    'New Balance',
    'Mizuno',
    'Under Armour',
    'Joma',
    'Sells',
    'Lotto'
]
proveedor_seleccionado = st.selectbox('Elige un proveedor:', proveedor)

# Filtrar el DataFrame según los valores seleccionados por el usuario
df_filtrado = df[
    (df['Liga'] == liga_seleccionada) &
    (df['Edad'] >= rango_edad[0]) &
    (df['Edad'] <= rango_edad[1]) &
    (df['Posicion'] == posicion_seleccionada) &
    (df['Proveedor'] == proveedor_seleccionado)
]

# Mostrar los resultados filtrados
if df_filtrado.empty:
    st.write('No se han encontrado jugadores que coincidan con los filtros seleccionados.')
else:
    st.write('Jugadores que coinciden con los filtros seleccionados:')
    st.dataframe(df_filtrado)