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
import difflib

#quality of life
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")
##end of import


#loading data into a dataframe (df)
data = pd.read_csv("Project/ml/Kaggle_1950_2019.csv")
df = pd.DataFrame(data).reset_index()

print(df.info())


## exploratory data analysis
#data cleaning
X = df.select_dtypes(np.number)
number_cols = list(X.columns)
print(number_cols)

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


##building the song recommendation program

#reformating input from an array of dictionaries to a dictionary of a list
def flatten_dict_list(dict_list):

    flattened_dict = defaultdict()

    for key in dict_list[0].keys():
        flattened_dict[key] = []
    
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)

    return flattened_dict

#retrieve information of searched song
def get_song_data(name, year):
    #TO_DO - replace == with .contains
    song_data = df[(df["track_name"].str.lower() == name.lower()) & (df['release_date'] == year)].reset_index()
    if song_data.empty:
        return None
    return song_data


#find the average values of the song list inputted
def get_mean_vector(song_list):

    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song['name'], song['year'])
        if song_data is None: 
            print('Warning: {} does not exist in database'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        np.delete(song_vector, np.s_[1:3], 1)
        song_vectors.append(song_vector)
    
    song_matrix = np.array(list(song_vectors))
    print(song_matrix)
    return np.mean(song_matrix, axis=0)




#actual recommendation function
def recommend_songs(song_list, n_songs=10):
    #metadata metrics tbd
    metadata_cols = ['track_name', 'release_date', 'artist_name']
    song_dict = flatten_dict_list(song_list)

    song_center = get_mean_vector(song_list)
    scaler = song_cluster_pipeline[0]

    #scaling xy for measuring distance (similarity)
    scaled_df = scaler.transform(df[number_cols])
    scaled_song_center = scaler.transform(song_center)
    distance = cdist(scaled_song_center, scaled_df, 'cosine')
    print(distance)
    index = list(np.argsort(distance)[:, :n_songs][0])

    rec_songs = df.iloc[index]
    #TO_DO: modify such that after deducting the input songs, the there are no less that 10 songs given
    rec_songs = rec_songs[~rec_songs['track_name'].isin(song_dict['name'])]
    formatted_rec = rec_songs[metadata_cols].to_dict(orient="records")
    return formatted_rec

#main
def main():
    rec_songs = recommend_songs([{'name': 'The Story of Us', 'year': 2010},
                {'name': 'Natalie', 'year': 2012},
                {'name': 'All Apologies', 'year': 1993},
                {'name': 'Stay Away', 'year': 1993}])
    print(rec_songs)

main()