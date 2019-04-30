
import Artist as at
import Track as track
# class that parse the json file retrieved from Spotify
class json_parser:

    # parses the first layer '[items]' hoding  list of artist
    def parse_search_item(self,json_file):
        search_results=((json_file['artists'])['items'])
        search_items =  self.parse_artist(search_results)
        return search_items

# parsing json file,retrieve relevant data and use Artist obj to store it then appending to a list
# return list of artist obj
    def parse_artist(self, search_results):
        artist_list = []
        for x in range(0, len(search_results)):
            name = (search_results[x])['name']
            follower = ((search_results[x])['followers'])['total']
            popularity = ((search_results[x])['popularity'])
            genres =((search_results[x])['genres'])
            images = self.try_find_image(search_results[x],-1)
            id = (search_results[x])['id']
            artist = at.Artist(name=name, follower=follower, popularity=popularity, genre=genres,image=images,id=id)

            artist_list.append(artist)

        return artist_list

# attempting to file a image for an artist, if nothing find return None obj
# return an url of artist picture, else return None
    def try_find_image(self, search_result, index):
        try:
            return ((search_result['images'])[index])['url']
        except:
            return None

    # parsing json file,retrieve a list of artist top trackcs
    # return list of track obj
    def parse_top_track(self,result):
        tracks = result['tracks']
        track_list =[]
        for x in range(0,len(tracks)):
            track_obj = None
            name = (tracks[x])['name']
            preview_url = (tracks[x])['preview_url']
            popularity = (tracks[x])['popularity']
            track_obj = track.Track(name=name, preview_url=preview_url, popularity=popularity)
            track_list.append(track_obj)
        return track_list

