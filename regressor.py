# el objetivo de este algoritmo es predecir el puntaje del icfes final

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import warnings
warnings.simplefilter("ignore")

data = pd.read_csv('data_model_segmented.csv')
puntajes = data[['MOD_RAZONA_CUANTITATIVO_PNAL',
       'MOD_LECTURA_CRITICA_PNAL', 'MOD_COMPETEN_CIUDADA_PNAL',
       'MOD_INGLES_PNAL', 'MOD_COMUNI_ESCRITA_PNAL', 'PUNT_GLOBAL']]









