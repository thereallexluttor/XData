# Importamos la librería Ydata_profiling para realizar análisis exploratorios de datos
from ydata_profiling import ProfileReport 

# Importamos la librería Streamlit para crear aplicaciones web interactivas
import streamlit as st 
import pandas as pd

# Importamos la librería Streamlit_pandas_profiling para integrar Ydata_profiling con Streamlit
from streamlit_pandas_profiling import st_profile_report 

import Xdata_DataManagement_Core_.Xdata_DataPreprocessing_engine_ as dc

@st.cache_data
def read_df(df):
    df = pd.read_csv(df)
    return df

@st.cache_data
def show_data(df):
    return df.head()    


def XactAi_Insights():
    page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #e5e5f7;
opacity: 0.8;
background-color: #565656;
opacity: 0.8;
background-color: #000000;
opacity: 1;
background-color: #989898;
opacity: 0.9;
background-color: #272727;
opacity: 0.9;
background-color: #000000;
opacity: 1;
background-color: #000000;
opacity: 1;
background-color: #000000;
opacity: 1;
background-image: radial-gradient(#272727 0.55px, #000000 0.55px);
background-size: 11px 11px;

}}
[data-testid="stSidebar"] > div:first-child {{
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
<*font color=‘red’>THIS TEXT WILL BE RED</*font>, unsafe_allow_html=True)
</style>
"""
    with st.sidebar: 
        st.markdown(page_bg_img, unsafe_allow_html=True)

        # Agregamos un título a la página
        st.title('Machine Learning Automatizado')

        # Agregamos un texto en formato Markdown para describir la función
        st.markdown('La magia de la IA a velocidades disruptivas.')
         
        st.title('Exploración de datos automatizada X.Insights')
        st.markdown('Explorar y analizar datos de manera automatizada y visualizar los resultados de forma interactiva.') 
        # load the file to do the real f*cking magic!
        # Agregamos un widget de Streamlit que permite al usuario subir un archivo CSV
        #data_file = st.file_uploader("Subir archivo .csv !")
        data_file = st.file_uploader("Subir archivo .csv !")

         # Se verifica si el archivo de datos se ha subido correctamente
    if data_file is not None:
            
            # Se carga el archivo CSV en un dataframe de pandas
            data_df = read_df(data_file)

            # Se instancia un objeto de la clase CleanDataframe para limpiar los datos
            cleaner = dc.DataPreprocessing_(data_df)

            # Se aplican las funciones para formatear los nombres de las columnas
            cleaner.name_formater()
        
            # Se limpia el dataframe con la función clean_dataframe()
            data_df_final = cleaner.clean_dataframe()

            #plot the dataframe
            pr = ProfileReport(data_df_final, explorative=True)

            #json_data = pr.to_json()
            #st.markdown(json_data)
            pr.to_file("your_report.pdf")
            st.title("Pandas Profiling in Streamlit")
            st.write(data_df_final.head())
            st_profile_report(pr)
