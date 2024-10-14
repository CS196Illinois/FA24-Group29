import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


# Load the CSV file data
def load_songs_data():
    # Get the absolute path of the current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory and then into the 'ml' folder to access the CSV file
    csv_path = os.path.join(base_dir, '..', 'ml', 'Kaggle_1950_2019.csv')
    
    print(f"Looking for file at: {csv_path}")  # Print the full path for debugging
    
    try:
        # Load the CSV file
        df = pd.read_csv(csv_path)
        # Print column names for debugging
        print("Loaded CSV columns: ", df.columns)

        # Clean column names (remove extra spaces)
        df.columns = df.columns.str.strip()

        # Ensure 'track_name' is present
        if 'track_name' not in df.columns:
            raise ValueError("'track_name' column is missing in the CSV file.")

        return df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise


# Flattening dictionary list to dictionary of lists
def flatten_dict_list(dict_list):
    flattened_dict = {}
    for key in dict_list[0].keys():
        flattened_dict[key] = []
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
    return flattened_dict

# Helper function to extract the song vector (based on user input)
def get_song_data(track_name, artist_name):
    df = load_songs_data()
    
    # Ensure both track_name and artist_name are provided
    if track_name is None or artist_name is None:
        print(f"Warning: Track name or artist name missing.")
        return None

    # Case-insensitive comparison and removing extra spaces
    track_name = track_name.strip().lower()
    artist_name = artist_name.strip().lower()

    # Make sure the columns in the dataframe are cleaned
    df['track_name'] = df['track_name'].str.strip().str.lower()
    df['artist_name'] = df['artist_name'].str.strip().str.lower()

    # Search for the track in the dataset based on track name and artist name
    song_data = df[(df['track_name'] == track_name) & (df['artist_name'] == artist_name)]

    if song_data.empty:
        return None
    return song_data

# Find the average values of the song list inputted
def get_mean_vector(song_list):
    song_vectors = []
    for song in song_list:
        # Fetch the song data based on track_name and artist_name (or whatever is passed)
        song_data = get_song_data(song['track_name'], song.get('artist_name'))
        
        if song_data is None:
            print(f"Warning: {song['track_name']} does not exist in the database")
            continue

        # Select only the numeric columns from the song data
        numeric_columns = song_data.select_dtypes(include=[np.number])

        if numeric_columns.empty:
            print(f"Warning: No numeric data found for {song['track_name']}")
            continue

        # Get the numeric data for the song and flatten it to 1D
        song_vector = numeric_columns.values.flatten()  # Flatten to avoid extra dimensions
        
        song_vectors.append(song_vector)
    
    if len(song_vectors) == 0:
        raise ValueError("No valid songs were found to calculate mean vector.")
    
    # Stack all vectors into a 2D array (n_songs, n_features)
    song_matrix = np.vstack(song_vectors)

    return np.mean(song_matrix, axis=0)  # This will return a 1D array of mean values

# Main recommendation function
def recommend_songs(song_list, n_songs=10):
    # Load the song data
    df = load_songs_data()

    # Only use numeric columns for the model
    X = df.select_dtypes(np.number)

    # Set up the machine learning model pipeline with scaler and kmeans
    song_cluster_pipeline = Pipeline([
        ('scaler', StandardScaler()), 
        ('kmeans', KMeans(n_clusters=20, verbose=False))
    ])

    # Fit the model on the data
    song_cluster_pipeline.fit(X)

    # Get the mean vector for the input songs
    try:
        song_center = get_mean_vector(song_list)
    except ValueError as e:
        print(f"Error: {e}")
        return []

    # Convert song_center to a DataFrame with the same columns as X
    song_center_df = pd.DataFrame([song_center], columns=X.columns)

    # Scale the input song vector using the scaler from the pipeline
    scaler = song_cluster_pipeline.named_steps['scaler']
    scaled_song_center = scaler.transform(song_center_df)

    # Scale the entire dataset
    scaled_df = scaler.transform(X)

    # Calculate cosine distances to find the closest songs
    distances = cdist(scaled_song_center, scaled_df, 'cosine')

    # Get the indices of the closest songs
    index = np.argsort(distances)[0][:n_songs]

    # Recommend songs, excluding the ones already in the input list
    rec_songs = df.iloc[index]
    rec_songs = rec_songs[~rec_songs['track_name'].isin([song['track_name'] for song in song_list])]

    # Return the recommended songs as a dictionary
    return rec_songs[['track_name', 'artist_name', 'genre']].to_dict(orient='records')