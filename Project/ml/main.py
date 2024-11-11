import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from collections import defaultdict

# Load and prepare the CSV file data
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
    
    # Validate required columns
    required_columns = ['track_name', 'artist_name', 'genre']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Required columns missing in CSV file: {', '.join(missing_columns)}")
    
    # Store valid values
    valid_artists = set(df['artist_name'].unique())
    valid_tracks = set(df['track_name'].unique())
    valid_genres = set(df['genre'].unique())
    
    # Encode categorical features
    le_artist = LabelEncoder()
    le_genre = LabelEncoder()
    
    df['artist_encoded'] = le_artist.fit_transform(df['artist_name'])
    df['genre_encoded'] = le_genre.fit_transform(df['genre'])
    
    # Create SongData instance with all necessary data
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
    """Validate that all input values exist in the dataset"""
    if track_name not in song_data.valid_tracks:
        raise ValueError(f"Track '{track_name}' not found in database")
    if artist_name not in song_data.valid_artists:
        raise ValueError(f"Artist '{artist_name}' not found in database")
    if genre not in song_data.valid_genres:
        raise ValueError(f"Genre '{genre}' not found in database")
    
# Flattening dictionary list to dictionary of lists
def flatten_dict_list(dict_list):
    flattened_dict = defaultdict(list)
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
    return flattened_dict

# Helper function to extract the song vector
def get_song_data(song_data, track_name=None, artist_name=None, genre=None):
    """Modified to handle independent searches for track, artist, and genre"""
    df = song_data.df
    
    # Convert inputs to lowercase for comparison
    if track_name:
        track_name = track_name.strip().lower()
    if artist_name:
        artist_name = artist_name.strip().lower()
    if genre:
        genre = genre.strip().lower()
    
    # Convert DataFrame columns to lowercase
    df['track_name'] = df['track_name'].str.strip().str.lower()
    df['artist_name'] = df['artist_name'].str.strip().str.lower()
    df['genre'] = df['genre'].str.strip().str.lower()
    
    # Build query conditions independently
    conditions = []
    if track_name:
        conditions.append(df['track_name'] == track_name)
    if artist_name:
        conditions.append(df['artist_name'] == artist_name)
    if genre:
        conditions.append(df['genre'] == genre)
    
    # If no conditions, return None
    if not conditions:
        return None
    
    # Combine conditions with OR instead of AND
    result = df[np.logical_or.reduce(conditions)]
    
    if not result.empty:
        return result
    
    return None

# Find the average values of the song list inputted
def get_mean_vector(song_data, song_list):
    song_vectors = []
    # Get all numeric columns including encoded categorical features
    numeric_columns = song_data.df.select_dtypes(np.number).columns
    
    # Make sure we include artist_encoded and genre_encoded
    required_features = ['artist_encoded', 'genre_encoded']
    for feature in required_features:
        if feature not in numeric_columns:
            raise ValueError(f"Required encoded feature {feature} not found in dataset")
    
    for song in song_list:
        song_data_result = get_song_data(
            song_data,
            song['track_name'],
            song.get('artist_name'),
            song.get('genre')
        )
        
        if song_data_result is None:
            continue
            
        # Get the feature vector including artist and genre encodings
        song_vector = song_data_result[numeric_columns].values
        if song_vector.size == 0:
            continue
            
        if len(song_vector) > 1:
            song_vector = np.mean(song_vector, axis=0)
        else:
            song_vector = song_vector[0]
            
        song_vectors.append(song_vector)
        
    if len(song_vectors) == 0:
        raise ValueError("No valid songs were found to calculate mean vector.")
        
    song_matrix = np.vstack(song_vectors)
    return np.mean(song_matrix, axis=0)

def recommend_songs(song_list, n_songs=10):
    song_data = load_songs_data()
    
    # Validate each song in the input list
    for song in song_list:
        track_name = song.get('track_name')
        artist_name = song.get('artist_name')
        genre = song.get('genre')
        
        if not all([track_name, artist_name, genre]):
            raise ValueError("Each song must have track_name, artist_name, and genre")
        
        validate_input(track_name, artist_name, genre, song_data)
    
    # Get all numeric columns including encoded features
    X = song_data.df.select_dtypes(np.number)
    
    # Ensure encoded features are included
    required_features = ['artist_encoded', 'genre_encoded']
    for feature in required_features:
        if feature not in X.columns:
            raise ValueError(f"Required encoded feature {feature} not found in dataset")
    
    # Create and fit the pipeline
    song_cluster_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=20, verbose=False))
    ])
    song_cluster_pipeline.fit(X)
    
    try:
        song_center = get_mean_vector(song_data, song_list)
        song_center_df = pd.DataFrame([song_center], columns=X.columns)
        
        scaler = song_cluster_pipeline.named_steps['scaler']
        scaled_song_center = scaler.transform(song_center_df)
        scaled_df = scaler.transform(X)
        
        distances = cdist(scaled_song_center, scaled_df, 'cosine')
        index = np.argsort(distances)[0][:n_songs]
        
        rec_songs = song_data.df.iloc[index]
        rec_songs = rec_songs[~rec_songs['track_name'].isin([song['track_name'] for song in song_list])]
        
        return rec_songs[['track_name', 'artist_name', 'genre']].to_dict(orient='records')
        
    except ValueError as e:
        print(f"Error: {e}")
        return []