""" Clase creada para el procesamiento veloz de paquetes de datos realizando 
limpiezas y eliminacion de imperfecciones que afectan la calidad de los dataframes.

El preprocesamiento es necesario y muy util a la hora de trabajar con datos y mas si 
el objetivo es vencer a los mejores analistas de datos del mundo.

Este es solo el comienzo de algo inmenso.

Hedinyer Mauricio Perucho Sequeda 22/05/2023"""


# import pandas lib to handle data and work fast
import pandas as pd
# import shuffle from sklearn
from sklearn.utils import shuffle

# this class is the core of the preprocessing work, 
# with this i can automate the hardwork 
class DataPreprocessing_:
    
    """ DataPreprocessing class is the most fastest class in data
    preprocessing, their work is clean and prepare datafreames in 
    the best way to get the best results (☞ﾟヮﾟ)☞ """

    #the init method
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
    
    #this method can transform any .csv file to an a dataframe
    def csv_to_dataframe_(self) -> pd.DataFrame:
        
        #Read the csv and transform it
        self.dataframe = pd.read_csv(self.dataframe)

        #Returns the dataframe
        return self.dataframe
    
    #this method can clean a dataframe and drop null rows
    def clean_dataframe(self):

        #Drop duplicated values
        self.dataframe = self.dataframe.drop_duplicates()

        #Drop null values
        self.dataframe = self.dataframe.dropna()

        #Drop NaN values in rows
        self.dataframe = self.dataframe.dropna(how = 'all')

        return self.dataframe
    
    #this method format and adjust the bad names of the columns in df
    def name_formater(self):
        
        # Limpiar los nombres de las columnas y obtener los mejores
        self.dataframe.columns = [x.lower().replace(" ","_").replace("?","")\
        .replace("-","_").replace(r"/","_").replace("\\","_").replace("%",'')\
        .replace(")","").replace(r"(","").replace("$","") for x in self.dataframe.columns]
        
        return self.dataframe   

    #thid method can retrieve the names of the dataframe columns
    def get_column_names(self):
        """
        Obtiene los nombres de las columnas del dataframe.
        
        Returns:
        - list: Lista de los nombres de las columnas del dataframe.
        """
        return list(self.dataframe.columns)
    
    #this method returns the dtypes of dataframe columns
    def get_columns_info(self):
          # Creamos un diccionario para almacenar la información de cada columna
          column_info = {}

          # Recorremos las columnas del dataframe
          for col in self.dataframe.columns:
            # Obtenemos el tipo de dato de la columna
            col_type = str(self.dataframe[col].dtype)

            # Guardamos el tipo de dato de la columna en la lista 'types'
            #self.dataframe.types.append(col_type)

            # Agregamos la información de la columna al diccionario
            column_info[col] = col_type
          return column_info
    
    #this method shuffle the dataframe and give us an oportunity to get the 
    #best results in our tool
    def shuffle_dataframe(self):
         shuffled_dataframe = shuffle(self.dataframe)
         shuffled_dataframe.reset_index(drop=True, inplace=True)
         return shuffled_dataframe
