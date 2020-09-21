import json
from statistics import mode

history0 = json.loads(open('./MyData/StreamingHistory0.json', 'r', encoding='utf8').read())
history1 = json.loads(open('./MyData/StreamingHistory1.json', 'r', encoding='utf8').read())

timePlayed = 0
artists = []
songs = []

for i in history0:
    timePlayed += int(i.get('msPlayed'))
    artists.append(i.get('artistName'))
    songs.append(i.get('trackName'))

for i in history1:
    timePlayed += int(i.get('msPlayed'))
    artists.append(i.get('artistName'))
    songs.append(i.get('trackName'))

for _ in range(0, 10):
    mostArtist = mode(artists)
    print(mostArtist + " " + str(artists.count(mostArtist)))

    while mostArtist in artists: 
        artists.remove(mostArtist)

print("\n\n")

for _ in range(0, 10):
    mostSongs = mode(songs)
    print(mostSongs + " " + str(songs.count(mostSongs)))

    while mostSongs in songs: 
        songs.remove(mostSongs)