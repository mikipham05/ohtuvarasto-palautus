import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url)
    players_data = response.json()

    players = []

    for player_dict in players_data:
        player = Player(player_dict)
        players.append(player)

    finnish_players = []

    for player in players:
        if player.nationality=="FIN":
            finnish_players.append(player)

    finnish_players.sort(
        key=lambda player: player.goals + player.assists,
        reverse=True
    )
    
    print("Finnish NHL players:")

    for player in finnish_players:
        print(
            f"{player.name}: {player.goals} goals, "
            f"{player.assists} assists, "
            f"points: {player.goals + player.assists} points"
        )

if __name__ == "__main__":
    main()
