from dotenv import load_dotenv
import os
from requests import post
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth

import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID') 
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://google.com/'
APP_SCOPE = 'user-library-read, playlist-modify-private, playlist-modify-public'

def get_playlists(client_id, client_secret, redirect_uri, scope):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=APP_SCOPE))


    user = sp.current_user()

    user_id = user['id']  # Extract the user ID from the user object

    playlists = sp.user_playlists(user_id)

    for idx, item in enumerate(playlists['items']):
        print(item['name'], item['id'])

def get_playlist_genres(client_id, client_secret, redirect_uri, scope, playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=APP_SCOPE))

    playlist_tracks = [] # empty list to store tracks in playlist

    playlist_genres = []

    results = sp.playlist_items(playlist_id)

    for idx, item in enumerate(results['items']):
        track = item['track']
        playlist_tracks.append(track)


    for track in playlist_tracks:
        artist_id = track['artists'][0]['id']
        artist_object = sp.artist(artist_id)

        for genre in artist_object['genres']:
            playlist_genres.append(genre)

    actual_playlist_genres = list(set(playlist_genres))
    return actual_playlist_genres


def get_playlist_track_ids(client_id, client_secret, redirect_uri, scope, playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=APP_SCOPE))

    playlist_tracks = []

    playlist_track_ids = []

    results = sp.playlist_items(playlist_id)

    for idx, item in enumerate(results['items']):
        track = item['track']
        playlist_tracks.append(track)

    for track in playlist_tracks:
        track_id = track['uri'].split(':')[2]
        playlist_track_ids.append(track_id)

    return(playlist_track_ids)



if __name__ == '__main__':
    get_playlists(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE)


""" if __name__ == '__main__':
    playlist_genres = get_playlist_genres(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,"")
    print(playlist_genres) """


