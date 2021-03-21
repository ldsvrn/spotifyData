import json
import sys
from statistics import mode

timePlayed = 0
artists = []
songs = []

for i in range(sys.maxsize): # Ouvre fichiers history, et oh putain je m'attendais pas a ce que ça marche
    try:
        history = json.loads(open('./MyData/StreamingHistory{}.json'.format(i), 'r', encoding='utf8').read())
        for i in history:
            timePlayed += int(i.get('msPlayed'))
            artists.append(i.get('artistName'))
            songs.append(i.get('trackName'))
    except:
        break

print("TOP 10 DES ARTISTES ({} artistes différents):".format(len(set(artists))))
for top in range(10):
    mostArtist = mode(artists)
    print("{}: L'artiste {} écouté {} fois.".format(top+1, mostArtist, artists.count(mostArtist)))

    while mostArtist in artists: 
        artists.remove(mostArtist)

print("\n\nTOP 10 DES TITRES: ({} titres différents, {} en tout)".format(len(set(songs)), len(songs)))

for top in range(10):
    mostSongs = mode(songs)
    print("{}: Le titre {} écouté {} fois.".format(top+1, mostSongs, songs.count(mostSongs)))

    while mostSongs in songs: 
        songs.remove(mostSongs)

print("\n\nTemps d'écoute total (arrondi): {}h\n".format(int(timePlayed / 3600000)))