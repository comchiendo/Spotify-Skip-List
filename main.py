import json
import os
path = os.getcwd()
os.chdir('my_spotify_data')
f = open('Streaming_History_Audio_2022-2024_1.json')

data = json.load(f)

skip_count = {}
song_name = "master_metadata_track_name"
play_time = "ms_played"
for i in data:
    if i["skipped"] == True or i[play_time] <= 30000:
        #print(i[song_name])

        if i[song_name] in skip_count:
            skip_count[i[song_name]] += 1
        else:
            skip_count[i[song_name]] = 1

sorted_count = sorted(skip_count.items(), key=lambda x:x[1], reverse=True)

#print(sorted_count)


for key in sorted_count[:10]:
    print(key[0], key[1])