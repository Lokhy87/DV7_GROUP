# DataFrame
st.subheader('Presentacion DataFrame')
st.dataframe(df.head())

#Selector de LIGA
st.subheader('Selecciona una Liga:')
liga_seleccionada = st.selectbox('Elige una liga:', ['LaLiga', '2ª División'])

# Selector FECHA CONTRATACION y FINAL
st.subheader('Fecha inicio y final del contrato:')
fecha_seleccionada = st.date_input('Elige una fecha de inicio de contrato:', min_value=datetime.date(2020, 1, 1), max_value=datetime.date.today())
fecha_seleccionada = st.date_input('Elige una fecha de finalizacion de contrato:', min_value=datetime.date(2020, 1, 1), max_value=datetime.date.today())

st.subheader('Seleccionar un rango de edad:')
# Crear un slider para seleccionar el rango de edad
rango_edad = st.slider(
    'Selecciona el rango de edad:',
    min_value = 18,  # Edad mínima
    max_value = 100,  # Edad máxima
    value = (18, 40),  # Rango inicial
    step = 1,  # Paso de 1 en 1
)
# Mostrar el rango de edad seleccionado
st.write(f'Has seleccionado el rango de edad: {rango_edad[0]} - {rango_edad[1]} años')