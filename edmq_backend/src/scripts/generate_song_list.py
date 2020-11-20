import requests
import json
import shazam_data

# Youtube API Request
part = 'snippet'
playlist_id = 'PLu-qQLnSm9zQwyCVh_c9uXJ6PDbEFBU8P'
api_key = 'AIzaSyAJtLJ-uNEpBLZqWHngF_Xpji2NmHFsqSQ'
playlist_url = 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=' + part + '&playlistId=' + playlist_id + '&key=' + api_key

# Load response into dictionary
yt_response = requests.get(playlist_url).text
playlist_dict = json.loads(yt_response)

video_id = []
video_items = playlist_dict['items']

song_list = {}
song_list['index'] = []

# Insert to json
for video in video_items:
    title = video['snippet']['title']
    id = video['snippet']['resourceId']['videoId']
    song_list['index'].append({
        'yt_title': title,
        'yt_id': 'https://www.youtube.com/watch?v=' + id,
        'song_title': shazam_data.get_title_artist(title)['title'],
        'song_artist': shazam_data.get_title_artist(title)['artist']
   })

with open(r'edmq_backend\src\data\songs.json', 'w') as output:
    json.dump(song_list, output)