# api_connector.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyConnector:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        ))

    def get_audio_features(self, track_name):
        results = self.sp.search(q=track_name, type="track", limit=1)
        if not results["tracks"]["items"]:
            return None
        track = results["tracks"]["items"][0]
        features = self.sp.audio_features(track["id"])[0]
        return {
            "track_name": track["name"],
            "artist": track["artists"][0]["name"],
            "bpm": features["tempo"],
            "energy": features["energy"],
            "valence": features["valence"],
            "danceability": features["danceability"],
            "acousticness": features["acousticness"],
            "instrumentalness": features["instrumentalness"],
            "genre": track["album"]["name"]  # temporaire
        }
