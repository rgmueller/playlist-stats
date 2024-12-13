import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_url):
    # Extract playlist ID from URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    
    # Get playlist tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    # Extract song names and artists
    songs = []
    for track in tracks:
        track_info = track['track']
        if track_info:  # Check if track exists (not None)
            song_name = track_info['name']
            # Get all artists for the track
            artists = [artist['name'] for artist in track_info['artists']]
            
            songs.append({
                'name': song_name,
                'artists': artists
            })
    
    return songs

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter your Spotify playlist URL: ")
    try:
        songs = get_playlist_tracks(playlist_url)
        print("\nPlaylist songs:")
        for i, song in enumerate(songs, 1):
            artists_str = ", ".join(song['artists'])
            print(f"{i}. {song['name']} by {artists_str}")
    except Exception as e:
        print(f"An error occurred: {e}")
