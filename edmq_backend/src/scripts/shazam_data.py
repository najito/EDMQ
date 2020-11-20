import requests
import json

# Monthly quota is 500 from RapidAPI
shazam_headers = {
    'x-rapidapi-key': "194d3fca7emsh5f18f2dac01d040p176829jsnf6975cc79831",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
shazam_url = "https://shazam.p.rapidapi.com/search"

def get_title_artist(term):
    d = {}
    querystring = {"term": term, "locale": "en-US", "offset": "0","limit": "1"}
    search_response = requests.request("GET", shazam_url, headers=shazam_headers, params=querystring).text
    search_dict = json.loads(search_response)
    d['title'] = search_dict['tracks']['hits'][0]['track']['title']
    d['artist'] = search_dict['tracks']['hits'][0]['track']['subtitle']
    return d