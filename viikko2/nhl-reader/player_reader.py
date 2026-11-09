
import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url)
        response.raise_for_status()

        players_data = response.json()

        return [Player(player) for player in players_data]
