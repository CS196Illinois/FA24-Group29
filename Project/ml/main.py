import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from collections import defaultdict

class SongData:
    def __init__(self, df, valid_artists, valid_tracks, valid_genres, artist_encoder, genre_encoder):
        self.df = df
        self.valid_artists = valid_artists
        self.valid_tracks = valid_tracks
        self.valid_genres = valid_genres
        self.artist_encoder = artist_encoder
        self.genre_encoder = genre_encoder

def load_songs_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '..', 'ml', 'Kaggle_1950_2019.csv')
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    
    required_columns = ['track_name', 'artist_name', 'genre']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Required columns missing in CSV file: {', '.join(missing_columns)}")
    
    valid_artists = set(df['artist_name'].unique())
    valid_tracks = set(df['track_name'].unique())
    valid_genres = set(df['genre'].unique())
    
    le_artist = LabelEncoder()
    le_genre = LabelEncoder()
    
    df['artist_encoded'] = le_artist.fit_transform(df['artist_name'])
    df['genre_encoded'] = le_genre.fit_transform(df['genre'])
    
    song_data = SongData(
        df=df,
        valid_artists=valid_artists,
        valid_tracks=valid_tracks,
        valid_genres=valid_genres,
        artist_encoder=le_artist,
        genre_encoder=le_genre
    )
    
    return song_data

def validate_input(track_name, artist_name, genre, song_data):
    if track_name not in song_data.valid_tracks:
        raise ValueError(f"Track '{track_name}' not found in database")
    if artist_name not in song_data.valid_artists:
        raise ValueError(f"Artist '{artist_name}' not found in database")
    if genre not in song_data.valid_genres:
        raise ValueError(f"Genre '{genre}' not found in database")

def flatten_dict_list(dict_list):
    flattened_dict = defaultdict(list)
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
    return flattened_dict

def get_song_data(song_data, track_name=None, artist_name=None, genre=None):
    df = song_data.df
    temp_df = df.copy()
    
    # Normalize input data and DataFrame columns
    if track_name:
        track_name = ' '.join(track_name.strip().lower().split())
        temp_df['track_name'] = temp_df['track_name'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    if artist_name:
        artist_name = ' '.join(artist_name.strip().lower().split())
        temp_df['artist_name'] = temp_df['artist_name'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    if genre:
        genre = ' '.join(genre.strip().lower().split())
        temp_df['genre'] = temp_df['genre'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    
    # Calculate similarity scores for each parameter
    similarity_score = pd.Series(np.ones(len(temp_df)), index=temp_df.index)
    
    if track_name:
        track_matches = (temp_df['track_name'] == track_name)
        similarity_score *= (track_matches * 3 + 1)  # Weight track matches more heavily
    
    if artist_name:
        artist_matches = (temp_df['artist_name'] == artist_name)
        similarity_score *= (artist_matches * 2 + 1)  # Weight artist matches
    
    if genre:
        genre_matches = (temp_df['genre'] == genre)
        similarity_score *= (genre_matches * 1.5 + 1)  # Weight genre matches
    
    # Sort by similarity score and return top matches
    temp_df['similarity_score'] = similarity_score
    result = temp_df.nlargest(5, 'similarity_score')
    
    if not result.empty:
        return df.loc[result.index]
    return None

def get_mean_vector(song_data, song_list):
    song_vectors = []
    numeric_columns = song_data.df.select_dtypes(np.number).columns
    
    for song in song_list:
        song_data_result = get_song_data(
            song_data,
            track_name=song.get('track_name', ''),
            artist_name=song.get('artist_name', ''),
            genre=song.get('genre', '')
        )
        
        if song_data_result is not None:
            song_vector = song_data_result[numeric_columns].values
            if song_vector.size > 0:
                # Weight the vectors based on match quality
                weights = song_data_result.get('similarity_score', np.ones(len(song_data_result)))
                weighted_vector = np.average(song_vector, axis=0, weights=weights)
                song_vectors.append(weighted_vector)
    
    if len(song_vectors) == 0:
        # If no matches found, use a random sample of songs
        random_sample = song_data.df.sample(min(5, len(song_data.df)))
        song_vectors = [random_sample[numeric_columns].mean().values]
    
    song_matrix = np.vstack(song_vectors)
    return np.mean(song_matrix, axis=0)

def recommend_songs(song_list, n_songs=10):
    song_data = load_songs_data()
    
    try:
        X = song_data.df.select_dtypes(np.number)
        
        song_cluster_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('kmeans', KMeans(n_clusters=20, verbose=False))
        ])
        song_cluster_pipeline.fit(X)
        
        song_center = get_mean_vector(song_data, song_list)
        song_center_df = pd.DataFrame([song_center], columns=X.columns)
        
        scaler = song_cluster_pipeline.named_steps['scaler']
        scaled_song_center = scaler.transform(song_center_df)
        scaled_df = scaler.transform(X)
        
        # Calculate combined distance metric
        distances = cdist(scaled_song_center, scaled_df, 'cosine')
        
        # Get recommendations avoiding input songs
        input_tracks = set(song['track_name'].lower() for song in song_list)
        recommendations = []
        idx = 0
        
        while len(recommendations) < n_songs and idx < len(song_data.df):
            current_idx = np.argsort(distances)[0][idx]
            current_song = song_data.df.iloc[current_idx]
            
            if current_song['track_name'].lower() not in input_tracks:
                recommendations.append(current_song[['track_name', 'artist_name', 'genre']].to_dict())
            
            idx += 1
            if idx >= len(song_data.df):
                break
        
        # If we still need more recommendations, add random songs
        while len(recommendations) < n_songs:
            random_song = song_data.df.sample(1).iloc[0][['track_name', 'artist_name', 'genre']].to_dict()
            if random_song['track_name'].lower() not in input_tracks:
                recommendations.append(random_song)
        
        return recommendations[:n_songs]
        
    except Exception as e:
        print(f"Error: {e}")
        # Return random recommendations if there's an error
        return song_data.df.sample(n_songs)[['track_name', 'artist_name', 'genre']].to_dict(orient='records')