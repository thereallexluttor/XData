# Importamos la librería Streamlit para crear aplicaciones web interactivas
import streamlit as st 
from streamlit_option_menu import option_menu 

# Importamos la librería Pandas para manipular los datos
import pandas as pd 

import Xdata_Functionalities_.X_insights_ as X_insights


# Creamos un menú desplegable en la barra lateral con el título "XactAI"
with st.sidebar:
    
    # Creamos las opciones del menú y les asignamos íconos para una mejor visualización
    selected = option_menu("XactAI", ["X.Insights", 'X.AutoML', 'X.Query'],   
        icons=['bar-chart-line', 'graph-up-arrow'], menu_icon="cast", default_index=1)


# Si se selecciona "X.Insights", se generará análisis exploratorio
if selected == "X.Insights":
    X_insights.XactAi_Insights()

# Si se selecciona "X.AutoML", se generará modelos de aprendizaje automático de forma automatizada
if selected == "X.AutoML":
    pass

# Si se selecciona "X.Query", se permitirá realizar consultas y búsquedas en el conjunto de datos
if selected == "X.Query":
    pass
