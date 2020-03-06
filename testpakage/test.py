import twitch

usernames = 'latteda_', 'twnickcan', 'miyaaoba'
helix = twitch.Helix('g3v9rj6v0t5cuthn57g3s9sd1sngmz')
for user in helix.users(usernames):
    print(f"Checking {user}")
    try:
        user.stream.type
    except twitch.helix.resources.streams.StreamNotFound:
        print('None')
        continue
    print(user.stream.data)
