from dotenv import load_dotenv
import os
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth
from Helpers import get_playlist_track_ids

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID') 
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://google.com/'
APP_SCOPE = 'user-library-read, playlist-modify-private, playlist-modify-public'

CUTOFF_YEAR = 1990

LIKED_LENGTH_50_ROUNDUP = 650  # *** set to the length of your liked songs playlist rounded up to the next number divisible by 50 as to include all liked songs respective of the 'current_user_saved_tracks' 50 max limit.

oldies_playlist_target_id = ""  # target playlist to add the old songs released before CUTOFF_YEAR

modern_playlist_target_id = ""  # target playlist to add the modern songs released after CUTOFF_YEAR

def sortLikedByReleaseYear(client_id, client_secret, redirect_uri, scope, liked_length_50_rd_up, before_year, oldies_playlist_target_id, modern_playlist_target_id):

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=APP_SCOPE))

    user = sp.current_user()
    user_id = user['id']  # Extract the user ID from the user object



    all_liked_songs = []  # list to append every all the liked songs into from every call of 'current_user_saved_tracks' fxn

    oldies_track_ids = [] # list to append all the songs in all_liked_songs that have 'release_date' before my desired CUTOFF_YEAR


    modern_track_ids =[]  # list to append all the song in all_liked_songs that have 'release_date' after my desired CUTOFF_YEAR



    for n in range(0, LIKED_LENGTH_50_ROUNDUP, 50):          # max rate limit of spotify api for current_user_saved_tracks for free dev apps in 50

        results = sp.current_user_saved_tracks(limit=50,offset=n)
        for idx, item in enumerate(results['items']):
            track = item['track']
            
            all_liked_songs.append(track)
            

    for track in all_liked_songs:
        release_year = int(track['album']['release_date'].split('-')[0])
        if release_year < CUTOFF_YEAR:
            oldies_track_ids.append(track['uri'].split(':')[2])

        else:
            modern_track_ids.append(track['uri'].split(':')[2])

    pre_oldies_target_playlist_track_ids = get_playlist_track_ids(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,oldies_playlist_target_id)

    pre_modern_target_playlist_track_ids = get_playlist_track_ids(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,modern_playlist_target_id)

    oldies_track_ids_actual = [track for track in oldies_track_ids if track not in pre_oldies_target_playlist_track_ids] # Removes any tracks that are already in the target playlist

    modern_track_ids_actual = [track for track in modern_track_ids if track not in pre_modern_target_playlist_track_ids] # Removes any tracks that are already in the target playlist


    for track in oldies_track_ids_actual:
        sp.user_playlist_add_tracks(user_id,oldies_playlist_target_id,[track],position=None)


    for track in modern_track_ids_actual:
        sp.user_playlist_add_tracks(user_id,modern_playlist_target_id,[track],position=None)


if __name__ == '__main__':
    sortLikedByReleaseYear(CLIENT_ID,CLIENT_SECRET,REDIRECT_URI,APP_SCOPE,LIKED_LENGTH_50_ROUNDUP, CUTOFF_YEAR, oldies_playlist_target_id, modern_playlist_target_id)