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

X = puntajes.drop(['PUNT_GLOBAL'],axis=1)
y = puntajes['PUNT_GLOBAL']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=0)
#iniciando a predecir con el modelo
model = LinearRegression().fit(X_train,y_train)
y_predict = model.predict(X_test)
print('calculando los coheficientes')
print()
print(f'coheficientes {model.coef_}')
print()
print('Calculando el score')
print(model.score(X_test,y_test))







