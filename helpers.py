# helpers.py
import spotipy
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics import pairwise_distances_argmin_min
import pickle

scaled_df = pd.read_csv("data/scaled_songs.csv")
with open('data/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('data/kmeans.pkl', 'rb') as f:
    kmeans = pickle.load(f)



def song_recom(client_id, client_secret,song):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
    col = ['acousticness', 'danceability', 'duration_ms', 'energy',
           'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
           'speechiness', 'tempo', 'time_signature', 'valence']
    results = sp.search(q=f'track:{song}', limit=1)
    track_uri = results['tracks']['items'][0]['uri']
    audio_features = sp.audio_features(track_uri)
    df35 = pd.DataFrame(audio_features)
    df35_features = df35[col]
    scaled_f = scaler.transform(df35_features)
    cluster = kmeans.predict(scaled_f)
    song, artist = song.split(' - ', 1)
    df_cluster = scaled_df[(scaled_df['cluster'] == cluster[0]) & 
                           (scaled_df['song_name'].str.lower() != song.lower()) & 
                           (scaled_df['artist'].str.lower() != artist.lower())]
    filtered_f = np.array(df_cluster[col], order='C')
    closest, _ = pairwise_distances_argmin_min(scaled_f,filtered_f)
    closest_song_name = df_cluster.iloc[closest[0]]['song_name']
    closest_artist = df_cluster.iloc[closest[0]]['artist']
    return '-'.join([closest_song_name, closest_artist])
