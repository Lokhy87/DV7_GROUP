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
            color: #1E90FF;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            color: #FF6347;
            font-size: 24px;
            font-weight: bold;
        }
        .section {
            background-color: #f2f2f2;
            padding: 10px;
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

# Subtítulo para la selección del rango de edad
st.subheader('Seleccionar un rango de edad:')
rango_edad = st.slider('Selecciona el rango de edad:', min_value=18, max_value=40, value=(18, 35), step=1)

# Subtítulo para la selección de posición
# st.subheader('Selecciona una posición:')
# posiciones = [
#     'Defensa central',
#     'Mediocentro',
#     'Delantero centro',
#     'Portero',
#     'Extremo derecho',
#     'Extremo izquierdo',
#     'Lateral derecho',
#     'Lateral izquierdo',
#     'Pivote',
#     'Mediocentro ofensivo',
#     'Mediapunta',
#     'Interior derecho',
#     'Interior izquierdo'
# ]
# posicion_seleccionada = st.selectbox('Elige una posición:', posiciones)

# Subtitulo para la seleccion de Valor Mercado
st.subheader('Selecciona un rango de Valor Mercado:')
valor_mercado_min = int(df['Valor Mercado'].min())
valor_mercado_max = int(df['Valor Mercado'].max())
rango_valor_mercado = st.slider('Selecciona el rango de Valor Mercado:', 
                                min_value=valor_mercado_min, 
                                max_value=valor_mercado_max, 
                                value=(valor_mercado_min, valor_mercado_max), 
                                step=100000)

# Seleccion proveedor 
st.subheader('Selecciona un agente:')
agentes = [
    "Agente no encontrado",
    "Promoesport",
    "YOU FIRST",
    "Wasserman",
    "CAA Stellar",
    "JV SPORTS",
    "IDUB GLOBAL",
    "InterStarDeporte",
    "LEADERBROCK",
    "Footfeel ISM",
    "Bahía Internacional",
    "Miembro de su familia",
    "Emartsoccer",
    "MESAS SPORT",
    "Niagara Sports ...",
    "WAKAI SPORTS",
    "LIAN Sports Group",
    "CAA Base Ltd",
    "Football Promotions ...",
    "Balance ...",
    "Antonio López ...",
    "MagicPlayers",
    "AC Talent",
    "Niagara Sur",
    "Goal Management",
    "Gesport Espizua SL",
    "Identity Sports",
    "Eugenio Botas ...",
    "IGdreamsfootball",
    "Toldra Consulting ...",
    "ROOF",
    "MRH Football Agency",
    "Best of You",
    "Global Ases",
    "Gestifute",
    "Universal Twenty Two",
    "Be Loyal by Ginés ...",
    "DCGLOBALSL",
    "IFM",
    "Intermedia Sport ...",
    "Joseba Diaz",
    "EMG Mundial",
    "Unique Sports Group",
    "Agente conocido - jugador menor de edad",
    "Roalza",
    "PROTIO SPORT",
    "RR-Soccer ...",
    "Sports&Life",
    "CANTERASPORT",
    "BOIM FOOTBALL ...",
    "Sin agente",
    "TACTIC GRUP - ...",
    "Sports and ...",
    "Manuel García ...",
    "EGGO Asesores ...",
    "SEG",
    "F.J.VILLAVERDE",
    "Gol International",
    "Excellence Sport",
    "FAIR SPORT MNG",
    "CONTROL ORIENTADO",
    "RGFOOTBALL",
    "ELITE INTERNACIONAL ...",
    "Team of Future",
    "De la Peña & ...",
    "Media Base Sports",
    "INVSPORT (Sergio ...)",
    "ABADSPORT",
    "SP",
    "VV Consulting",
    "Rioja Cermeño S.L.",
    "Acción Sport",
    "33 Sport",
    "ESN",
    "Kemari",
    "Augustin Jimenez",
    "ACE",
    "BY AND FOR",
    "LA PLAYERS",
    "Proeleven S.A.",
    "BestFoot FM",
    "Alinea",
    "Phsport",
    "B1G Talent",
    "Footfay",
    "#LEADERS",
    "Joes Blakborn",
    "Pedro Bravo - ...",
    "Team Raiola",
    "Miguel Pedrajo",
    "IS SPORTS AGENCY",
    "Bertolucci Sports",
    "MIV GESTFUT",
    "FutureBall",
    "ADM PRO",
    "MSSports",
    "PINTEX SPORTS AGENCY",
    "MadeinFootball",
    "Hernan Berman",
    "HCM Sports ...",
    "Stirr Associates",
    "Ivan Cristovinho",
    "Universal Sport",
    "7DS",
    "DV7 Management",
    "Roc Nation Sports",
    "José Vicente ...",
    "MG",
    "Stars & Friends",
    "Nordic Sky",
    "La Squadra Sports",
    "LINK SPORTS",
    "NTS Management",
    "Feel Winner",
    "Nomi Sports",
    "Elite Management ...",
    "Fernando Hidalgo",
    "ADM Esporte",
    "Blueprivate ...",
    "KHALENA SPORT",
    "JONATHAN SÁNCHEZ",
    "Gallea Gestion S.A",
    "Roberto Tukada",
    "Free Football",
    "PURE",
    "Invictus Team",
    "Carmelo Sánchez",
    "Guastadisegno",
    "FSB – ...",
    "UJ Football Talent",
    "Christophe Henrotay",
    "SeiSei Football",
    "Sports360 GmbH",
    "KIN Partners",
    "DLT Sports Group",
    "Int. Sport Management s.r.o.",
    "PARRI GROUP",
    "ML3 Football",
    "Soccertalk GmbH",
    "Pavel Andreev",
    "STV",
    "Sp international",
    "2SAgency",
    "FUTBOL21 AGENCY",
    "Aneke/PMG",
    "ROGON",
    "Top Sport Medium",
    "V4S",
    "ND SPORTS MANAGEMENT",
    "Signature - ISCM AG",
    "Carlos Bilicich",
    "Solbakken / Player ...",
    "S.O.M FOOTBALL",
    "Master Talents",
    "Interplayers",
    "380amk",
    "Elite FA",
    "AIS Football",
    "Fútbol LLave",
    "PCR Sports",
    "LGT Football",
    "Panthera Sports",
    "Jose Levis Manager",
    "PUM",
    "Sport Interactive ...",
    "JHSEVENSPORTSCOMPANY...",
    "Futuro Global ...",
    "Darren Dein",
    "Football Capital",
    "Rafaela Pimenta",
    "Primotempo",
    "BS Group - BS Law",
    "Keypass AS",
    "DRL",
    "TRIPLE MATCH",
    "AYMO Football ...",
    "SIELLO FOOTBALL ...",
    "Fabián Bustos",
    "GBG Global Business ...",
    "HC",
    "JCRsport",
    "Prosport ...",
    "AMS CONSULTING",
    "BDN",
    "INSUA GROUP",
    "BY Sport Consulting",
    "SPORT INVEST",
    "Lion Volt",
    "management 360",
    "K2K Sports ...",
    "Gianni Vitali",
    "Eleven Talent Group",
    "Field Management",
    "After90Group",
    "Axia Sports ...",
    "BHM Sports Agency",
    "Soccer Promotions",
    "Quinas",
    "KV Sports Management",
    "JEB ENTERTAINMENT ...",
    "11MANGMT",
    "LF Sport Management",
    "20 Sport",
    "MG MEDIATOR TRANSFER",
    "Fabryka Futbolu",
    "BFM",
    "OKON",
    "OFSPORTS",
    "Soccersport",
    "MFS - Managing ...",
    "Youssoupha Fall",
    "REVOLUTION Football ...",
    "EF11 SL",
    "Kick Off Management",
    "Talents Sports",
    "MRP.POSITIONUMBER",
    "F&H Sport Management",
    "PASCUAL FERNANDO ...",
    "AGREF",
    "Faro Sports",
    "Hexagon",
    "Equipo TMA",
    "Vibra Futbol",
    "PRI Sports",
    "12 MANagement",
    "CID Marinescu",
    "Scoutfutbol",
    "Marcio Bittencourt ...",
    "Universal Football",
    "AK10 STARS",
    "INTERNATIONAL ...",
    "Adrián del Nido",
    "Borja Couce",
    "Carp Football ...",
    "BG Sports",
    "GR Sports",
    "Dvitex Sports ...",
    "Premier Fútbol",
    "MC Striker",
    "Marcelo Tejera",
    "Igor Gluscevic",
    "Proyecta Players",
    "Miha Mlakar",
    "Footwork",
    "SportsMaxi ...",
    "Sport Agency 4U",
    "Active Action Asia",
    "1930 S&L",
    "World Soccer Agency",
    "VIDA 11",
    "Galka Scouting ...",
    "Jorge Llagostera ...",
    "Impacto Deportivo",
    "RMD Sport Manager",
    "Pro Evolution ...",
    "Podium Trade",
    "Elenko Sports Ltda.",
    "SMI SPORTS ...",
    "Global Compensation",
    "Un1que Football",
    "SimaSport Soccer",
    "CM Sports Agency",
    "People In Sport",
    "NexSt11",
    "Nono lora",
    "Aclama",
    "AXISFUT",
    "H2 Agency"
]
agente_seleccionado = st.selectbox('Elige un agente:', agentes)

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
    # (df['Posicion'] == posicion_seleccionada) &
    (df['Proveedor'] == proveedor_seleccionado) &
    (df['Valor Mercado'] >= rango_valor_mercado[0]) &
    (df['Valor Mercado'] <= rango_valor_mercado[1]) &
    (df['Agente'] == agente_seleccionado)
]

# Mostrar los resultados filtrados
if df_filtrado.empty:
    st.write('No se han encontrado jugadores que coincidan con los filtros seleccionados.')
else:
    st.write('Jugadores que coinciden con los filtros seleccionados:')
    st.dataframe(df_filtrado)