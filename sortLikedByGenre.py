from dotenv import load_dotenv
import os
from requests import post
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Helpers import get_playlist_genres, get_playlist_track_ids

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID') 
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://google.com/'
APP_SCOPE = 'user-library-read, playlist-modify-private, playlist-modify-public'

LIKED_LENGTH_50_ROUNDUP = 650  # <------ SET THIS to the length of your liked songs playlist rounded up to the next number divisible by 50 as to include all liked songs respective of the 'current_user_saved_tracks' 50 max limit.
                                         # example: If your Liked Songs playlist has 627 track set this value to 650.

target_playlist_id = "" # <------ ADD YOUR target playlist id that will have current genres identified to pull genre matches from Liked Songs

def sortLikedByGenre(client_id, client_secret, redirect_uri, scope,liked_length_50_rd_up, target_playlist_id):

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=APP_SCOPE))



    user = sp.current_user()
    user_id = user['id']  # Extract the user ID from the user object

    all_liked_songs = []  # list to append every all the liked songs into from every call of 'current_user_saved_tracks' fxn

    tracks_to_add_by_genre = []

    target_playlist_genre_list = get_playlist_genres(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,target_playlist_id)

    for n in range(0, LIKED_LENGTH_50_ROUNDUP, 50):          # max rate limit of spotify api for current_user_saved_tracks for free dev apps in 50

        results = sp.current_user_saved_tracks(limit=50,offset=n)
        for idx, item in enumerate(results['items']):
            track = item['track']
            
            all_liked_songs.append(track)

        
    for track in all_liked_songs:
        
        artist_id = track['artists'][0]['id']
        artist_object = sp.artist(artist_id)

        for genre in artist_object['genres']:
            if genre in target_playlist_genre_list:
                tracks_to_add_by_genre.append(track['uri'].split(':')[2])

    tracks_by_genre_list_actual = list(set(tracks_to_add_by_genre))

    pre_target_playlist_track_ids = get_playlist_track_ids(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,target_playlist_id)

    tracks_to_add_final = [track for track in tracks_by_genre_list_actual if track not in pre_target_playlist_track_ids] # Removes any tracks that are already in the target playlist

    for track in tracks_to_add_final:
        sp.user_playlist_add_tracks(user_id,target_playlist_id,[track],position=None)





if __name__ == '__main__':
    sortLikedByGenre(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,LIKED_LENGTH_50_ROUNDUP,target_playlist_id)


















