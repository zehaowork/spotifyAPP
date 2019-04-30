from PIL import Image
import requests
from io import BytesIO
import api_request

# Arist class store relevant info of an artist,including its top tracks
class Artist:

    def __init__(self, name, follower, popularity, genre, image,id):
        self.name = name
        self.follower = follower
        self.popularity = popularity
        self.genre = self.format_genre(genre)
        self.image = self.get_img_from_url(image)
        self.id = id
        self.tracks = self.artist_top_track()

# format the genre list, concatenate genres
    def format_genre(self, genre):
        if len(genre)!=0:
            string_genre = genre[0]
            if len(genre)>1:
                for x in range(1,len(genre)):
                    string_genre = string_genre+", "+genre[x]
            return string_genre

# get retrieve image from the url
    def get_img_from_url(self, image_url):
        if image_url is not None:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            return img
        else:
            return Image.open('default_profile.jpg')

# request for artist's top tracks using Spotify Web API
    def artist_top_track(self):
        track = api_request.request_artist_track(self.id)
        print(self.name)


        return track

