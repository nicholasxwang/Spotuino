from SwSpotify import spotify
import os
import warnings
warnings.filterwarnings("ignore")
def clear():
    os.system('clear')
def get_song(old_song):
    try:
        current_song = spotify.song()
    except:
        current_song = "No Song is being Played Right Now! Go to Spotify and play some music!"

    #if current_song != old_song:
    clear()
    print(current_song)
    return current_song

song = ""
while True:
    song = get_song(song)