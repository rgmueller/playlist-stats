import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
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
    
    # Get release dates and calculate ages
    current_year = datetime.now().year
    ages = []
    
    for track in tracks:
        release_date = track['track']['album']['release_date']
        release_year = int(release_date.split('-')[0])
        age = current_year - release_year
        ages.append(age)
    
    return np.mean(ages)

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter your Spotify playlist URL: ")
    try:
        average_age = get_playlist_tracks(playlist_url)
        print(f"The average age of songs in your playlist is {average_age:.1f} years")
    except Exception as e:
        print(f"An error occurred: {e}")
