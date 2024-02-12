# el objetivo de este algoritmo es predecir que estudiantes se desempeñaron en bajo, medio y alto con respecto al puntaje funal.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data_model_segmented.csv')


x = data.drop(['GRUPO'],axis=1)
y = data['GRUPO']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=1)

knn_class = KNeighborsClassifier().fit(x_train, y_train)
knn_prediction = knn_class.predict(x_test)
print('Calculando el score')
print('SCORE -->> : ', accuracy_score(knn_prediction, y_test))
