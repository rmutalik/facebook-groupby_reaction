import facebook
import webbrowser

# get short-lived access token
token = ""                         # Put your access token here
username = "Freddie Mercury"       # Put your first and last name, separated by a space

# use token to get access to Graph API
graph = facebook.GraphAPI(access_token=token)

# Get album name
album_id = '123456789'
album = graph.get_object(id=album_id, fields='name')
print(album['name'])

# Get photos in the album
photos = graph.get_object(id=album_id+'/photos')
photos_list = []
photo_id = photos['data']

# Collect all the pictures together
for i in photo_id:
    photos_list.append(i['id'])

# Group pictures by likes and reactions
likes_loves_list = []
for pid in photos_list:
    likes = graph.get_connections(id=pid, connection_name='likes')
    reactions = graph.get_connections(id=pid, connection_name='reactions')
    if likes['data'] and likes['data'][0]['name'] == username:
        likes_loves_list.append(pid)
    if reactions['data'] and reactions['data'][0]['name'] == username and reactions['data'][0]['type'] == 'LOVE':
        likes_loves_list.append(pid)
print("Likes and Loves from me: ", likes_loves_list)

# open each picture in a new tab
for pid in likes_loves_list:
    photo = graph.get_object(id=pid, fields='picture')
    webbrowser.open_new_tab(photo['picture'])
