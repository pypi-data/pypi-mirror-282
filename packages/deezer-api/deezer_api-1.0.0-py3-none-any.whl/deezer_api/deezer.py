# deezer_api/deezer.py

import requests

class DeezerAPI:
    def __init__(self):
        self.base_url = "https://api.deezer.com"

    def fetch_deezer_data(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def search(self, query="eminem"):
        return self.fetch_deezer_data("search", params={'q': query})

    def get_album(self, album_id="302127"):
        return self.fetch_deezer_data(f"album/{album_id}")

    def get_editorial(self):
        return self.fetch_deezer_data("editorial")

    def get_chart(self):
        return self.fetch_deezer_data("chart/0")

    def get_artist(self, artist_id="27"):
        return self.fetch_deezer_data(f"artist/{artist_id}")

    def get_track(self, track_id="3135556"):
        return self.fetch_deezer_data(f"track/{track_id}")

    def get_radio(self):
        return self.fetch_deezer_data("radio")

    def get_playlist(self, playlist_id="908622995"):
        return self.fetch_deezer_data(f"playlist/{playlist_id}")

    def get_infos(self):
        return self.fetch_deezer_data("infos")

    def get_genre(self):
        return self.fetch_deezer_data("genre")

    def get_user(self, user_id="5557228304"):
        return self.fetch_deezer_data(f"user/{user_id}")
      
