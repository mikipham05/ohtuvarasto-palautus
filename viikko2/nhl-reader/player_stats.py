class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [
            player for player in self.players
            if player.nationality == nationality
        ]

        return sorted(
            filtered_players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )