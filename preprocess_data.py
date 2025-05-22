import pandas as pd
import logging
import warnings
import os

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PreprocessData:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        logging.info("Data cargada exitosamente.")
        
    def clean_data(self):
        logging.info("Iniciando limpieza de la data.")
        
        columns_to_keep = [
            'MOD_INGLES_PNAL', 
            'MOD_COMUNI_ESCRITA_PNAL', 
            'MOD_COMPETEN_CIUDADA_PNAL', 
            'MOD_LECTURA_CRITICA_PNAL',
            'MOD_RAZONA_CUANTITATIVO_PNAL',
            'PUNT_GLOBAL',
            'id_unico'
        ]
        
        # Eliminar todas las columnas excepto las especificadas
        all_columns = self.data.columns.tolist()
        columns_to_drop = [col for col in all_columns if col not in columns_to_keep]
        
        initial_cols_count = len(self.data.columns)
        self.data = self.data.drop(columns=columns_to_drop, errors='ignore')
        logging.info(f"Columnas resultantes: {self.data.columns.tolist()}")
        
        # Eliminar registros vacíos (NaN)
        initial_rows_for_na = len(self.data)
        self.data.dropna(inplace=True)
        rows_removed_na = initial_rows_for_na - len(self.data)
        logging.info(f"Se eliminaron {rows_removed_na} filas con valores vacíos.")

        # Eliminar registros duplicados
        initial_rows_for_duplicates = len(self.data)
        self.data.drop_duplicates(inplace=True)
        rows_removed_duplicates = initial_rows_for_duplicates - len(self.data)
        logging.info(f"Se eliminaron {rows_removed_duplicates} filas duplicadas.")
        
        logging.info(f"Dataset limpio: {self.data.shape}")
    
    def save_data(self, output_directory, file_name):
        # guardar data limpia
        logging.info("Guardando el dataset limpio.")
        os.makedirs(output_directory, exist_ok=True)
        
        output_path = os.path.join(output_directory, file_name)
        self.data.to_csv(output_path, index=False)
        logging.info(f"Dataset limpio guardado exitosamente en: {output_path}")


    def run(self, file_path, output_directory, output_file_name):
        self.load_data(file_path)
        self.clean_data()
        self.save_data(output_directory, output_file_name)

if __name__ == "__main__":
   
   csv_file_path = "/Users/davinci/Desktop/proyecto_icfes/data_project/raw_data/data.csv" 
   output_data_directory = "/Users/davinci/Desktop/proyecto_icfes/data_project/data_processed"
   clean_file_name = "data_clean.csv"
   processor = PreprocessData()
   processor.run(csv_file_path, output_data_directory, clean_file_name)
        

