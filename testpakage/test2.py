from threading import Event, Thread
import time
import twitch

usernames = 'latteda_', 'twnickcan', 'miyaaoba'
def main():
    starttime = time.time()

    while True:
        mainloop()
        time.sleep(300.0 - (time.time() - starttime % 300.0))
def mainloop():
    print("running")
    global streams_current

    print(f"Current list of stream ids: {list(streams_current.keys())}")
    stream_new = get_streams()

    streamids_status = compare_streams(streams_current, streams_new)

    announce_streams(streamids_status, streams_current, streams_new)

    streams_current = streams_new

def get_streams():
    streams = {}
    ClientID = 'g3v9rj6v0t5cuthn57g3s9sd1sngmz'
    width = 640
    height = 360
    helix = twitch.Helix(ClientID)

    for user in helix.users(usernames):
        try:
            user.stream.type
        except twitch.helix.resources.streams.StreamNotFound:
            print('None')
            continue
        print(user.stream.data)

        if res['data'] != []:
            stream_id = res['data'][0]['id']
            streams[stream_id] = {}
            streams[stream_id]['username'] = user
            streams[stream_id]['url'] = 'https://www.twitch.tv/' + user
            streams[stream_id]['game'] = res['data'][0]['user_name']
            streams[stream_id]['status'] = res['data'][0]['title']
            streams[stream_id]['preview_l'] = res['data'][0]['thumbnail_url']
            streams[stream_id]['preview_l'] = streams[stream_id]['preview_l'].replace('{width}', '640')
            streams[stream_id]['preview_l'] = streams[stream_id]['preview_l'].replace('{height}', '360')
            print(streams[stream_id]['preview_l'.format(width, height)])


