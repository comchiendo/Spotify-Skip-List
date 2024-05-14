import json
import os
path = os.getcwd()
os.chdir('my_spotify_data')
f = open('Streaming_History_Audio_2022-2024_1.json')

data = json.load(f)

skip_count = {}
for i in data:
    if i["skipped"] == True:
        print(i["master_metadata_track_name"])
        
        if i["master_metadata_track_name"] in skip_count:
            skip_count[i["master_metadata_track_name"]] += 1
        else:
            skip_count[i["master_metadata_track_name"]] = 1

#print(skip_count)
print(skip_count.values())