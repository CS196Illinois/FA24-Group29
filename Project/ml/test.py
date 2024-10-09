##imports
#data wrangling
import os
import numpy as np
import pandas as pd

#visualization
import seaborn as sns
import plotly.express as px 
import matplotlib.pyplot as plt

#ml
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist

#quality of life
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")
##end of import


#loading data into a dataframe (df)
df = pd.read_csv("Project/ml/Kaggle_1950_2019.csv")

print(df.info())


## exploratory data analysis
#data cleaning
X = df.select_dtypes(np.number)
number_cols = list(X.columns)

#calling pipeline function & specifying kmeans algo
song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                 ('kmeans', KMeans(n_clusters=20, verbose=False))]
                                 , verbose=False)

#fitting hyperparameters in model, then using model to return predict
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)

#adding cluster as a new property to df
df['cluster_label'] = song_cluster_labels

print(df)

#principal component analysis (capturing similarity between songs through proximity of xy coordinate)
pca_pipeline = Pipeline([('scaler', StandardScaler()), 
                         ('PCA', PCA(n_components=2))])
song_embedding = pca_pipeline.fit_transform(X)
print(song_embedding)

#visualization of PCA
projection = pd.DataFrame(columns=['x', 'y'], data=song_embedding)
projection['title'] = df['track_name']
projection['cluster'] = df['cluster_label']

fig = px.scatter(
    projection, x='x', y='y', color='cluster', hover_data=['x', 'y', 'title']
)
fig.show()
## end of exploratory data analysis
