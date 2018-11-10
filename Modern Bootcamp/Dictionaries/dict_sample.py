playlist = {
    'title': 'time of our lives',
    'creator': 'jon brown',
    'songs': [
        {'title': 'song1', 'artist': ['bobby brown'], 'length': 2.5},
        {'title': 'song2', 'artist': ['snoopy dog', 'ice cube'], 'length': 3.0},
        {'title': 'ballad1', 'artist': ['pat smith'], 'length': 4.0}
    ]
}

total_length = 0
for time in playlist['songs']:
    total_length += time['length']

print(total_length)


