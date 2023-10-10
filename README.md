# SpotifyLikedSortProj

## Introduction

SpotifyLikedSortProj is a Python project that provides two main functions to help you better organize your liked songs on Spotify. I created the tools because I had a need to organize/sort all the songs from my Liked Songs playlist into many personal curated playlists I have.The project utilizes the `spotipy` Python module, which interacts with the Spotify Web API to fetch and manage your Spotify data.

## Prerequisites

Before you start using the functions in this project, make sure you have the following:

1. Python installed on your system.
2. The required Python libraries, including `spotipy`, which are listed in the `requirements.txt` file in this repository. You can install them using the following command:
   
   pip install -r requirements.txt
   

3. Create a Spotify App:
   - Go to https://developer.spotify.com/ and log in with your Spotify account.
   - Create a new app in the Spotify Developer Dashboard.
   - Once the app is created, set the redirect URL (I suggest http://google.com as used in the code) and note down the `Client ID` and `Client Secret`. You will need these to authenticate the Spotify API calls.

4. Set Up Environment Variables:
   - Create a `.env` file in the project directory.
   - Add the following lines to the `.env` file, replacing `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with the actual values from your Spotify app:
     
     CLIENT_ID=YOUR_CLIENT_ID
  
     
     CLIENT_SECRET=YOUR_CLIENT_SECRET
     
   - The project uses the `dotenv` library to load these environment variables for authentication.

## Function 1: sortLikedByReleaseYear.py

This function retrieves all your liked songs from Spotify and sorts them into two playlists: "Oldies" and "Modern" based on a `CUTOFF_YEAR`. All songs released before the `CUTOFF_YEAR` will be added to the "Oldies" playlist, and all songs released on or after the `CUTOFF_YEAR` will be added to the "Modern" playlist.

### Usage

1. Ensure you have the correct playlist ids in the target_id variables, these playlist ids can be retrieved by running Helpers.py which utilizes the get_playlists function to output all your playlist titles and ids.
2. Open `sortLikedByReleaseYear.py` and replace the `CUTOFF_YEAR` variable with the desired year to separate oldies from modern songs.

## Function 2: sortLikedByGenre.py

This function takes a target playlist, fetches its genres, and then adds any song from your liked songs that matches those genres to the target playlist.

### Usage

1. Ensure you have the correct playlist ids in the target_id variables, these playlist ids can be retrieved by running Helpers.py which utilizes the get_playlists function to output all your playlist titles and ids.
2. Open `sortLikedByGenre.py` and replace the `target_playlist_id` variable with the `playlist_id` of the target playlist.

## Helpers.py

The `Helpers.py` file contains a `get_playlists` function that allows you to retrieve all your playlist's titles and ids. The ids can then be copied and inserted into the desired target variables.

## Getting Started

To get started, follow the steps below:

1. Clone this repository to your local machine.
2. Set up the required Python environment by installing the necessary dependencies from the `requirements.txt` file.
3. Create a Spotify app at https://developer.spotify.com/ and obtain the `Client ID` and `Client Secret`, also I suggest setting the redirect URL of the app to 'http://google.com' as assigned in the code.
4. Create a `.env` file in the project directory and add the `Client ID` and `Client Secret` as environment variables as described above.
5. Follow the usage instructions provided for each of the main functions (`sortLikedByReleaseYear.py` and `sortLikedByGenre.py`).
6. Use the information from the `Helpers.py` file to get the `playlist_id`s for your target playlists.

## Note
******* It is HIGHLY RECOMMENDED that you create some test playlists on your account first to get an idea of how they work/run to avoid any mishaps with personal playlists.
This project is provided as-is and comes with no warranties or support. Please use it responsibly and ensure you have appropriate permissions to modify your Spotify playlists.

**Happy organizing!**