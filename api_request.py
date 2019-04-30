import requests
import json_parser as jsp



# request on Spotify Web API search
# param: artist name
# return list of parsed artist info
def search_artist(artist_name):
    headers = {"Accept": "application/json", "Content-Type": "application/json",
                'Authorization': "Bearer " + access_token}
    params = (
            ('q', artist_name),
            ('type', 'artist'),
             ('limit', '20'),
            )
    artist_info = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params).json()
    parsed_artist_into = parser.parse_search_item(artist_info)
    return parsed_artist_into

# request for the access token for the Spotify API
# return Access Token of Spotify API
def get_token():
    client_id = "926a2cbcd1b94970859e1ac6b3a56630"
    client_secret = "95bb4cf625f64c008b7873e6b5970811"
    grant_type = 'client_credentials'
    request_token_url = 'https://accounts.spotify.com/api/token'
    body_param = {'grant_type': grant_type}
    response = requests.post(request_token_url, data=body_param, auth=(client_id, client_secret)).json()
    return response

# send HTTP request fo Artist track
# param: artist_id
# return artist track
def request_artist_track(artist_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + access_token,
    }

    params = (
        ('country', 'SE'),
    )
    response = requests.get('https://api.spotify.com/v1/artists/'+artist_id+'/top-tracks', headers=headers,
                            params=params).json()
    parsed_result = parser.parse_top_track(response)

    return parsed_result


# stores access token
access_token = get_token()["access_token"]
# creates a json parser obj
parser = jsp.json_parser()





