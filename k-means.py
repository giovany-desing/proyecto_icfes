import pandas as pd
from sklearn.cluster import MiniBatchKMeans

import seaborn as sns
import matplotlib.pyplot as plt
import logging

my_model = 'K-means'
data = pd.read_csv('data_model.csv')
X = data

print(X.dtypes)

