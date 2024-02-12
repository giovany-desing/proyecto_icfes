import pandas as pd
from sklearn.cluster import MiniBatchKMeans

import seaborn as sns
import matplotlib.pyplot as plt
import logging

my_model = 'K-means'
data = pd.read_csv('data_model.csv')
X = data

kmeans = MiniBatchKMeans(n_clusters=3, batch_size=8).fit(X)
print(f" Ejecutano -> {my_model}")
data['GRUPO'] = kmeans.predict(X)
print('Graficando el resultado')
sns.histplot(data=data, x='PUNT_GLOBAL', hue='GRUPO', multiple='stack')
plt.show()
data.to_csv('data_model_segmented.csv', index = False)

