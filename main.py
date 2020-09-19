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

mostArtist = mode(artists)
mostSongs = mode(songs)

print("L'artiste le plus écouté est: {}, écouté en tout {} fois.".format(mostArtist, artists.count(mostArtist)))
print("La chanson la plus écoutée est: {}, écoutée en tout {} fois.".format(mostSongs, songs.count(mostSongs)))
print("Temps d'écoute total (arrondi): {}h\n".format(int(timePlayed / 3600000)))

question = input('Voir combien de fois une chanson a été écoutée (case sensible): ')
print('La chanson "{}" a été écoutée {} fois.\n'.format(question, songs.count(question)))

question2 = input('Voir combien de fois un artiste a été écouté (case sensible): ')
print('L\'artiste "{}" a été écouté {} fois.\n'.format(question2, artists.count(question2)))