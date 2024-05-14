import json
import os
path = os.getcwd()
os.chdir('my_spotify_data')
f = open('Streaming_History_Audio_2022-2024_1.json')

data = json.load(f)

for i in data:
    if i["skipped"] == True:
        print(i["master_metadata_track_name"])
