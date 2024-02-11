# el objetivo de este algoritmo es predecir que estudiantes se desempeñaron en bajo, medio y alto con respecto al puntaje funal.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data_model_segmented.csv')


