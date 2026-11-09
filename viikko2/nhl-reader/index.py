
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()

    nationality = Prompt.ask(
        "Enter nationality (e.g. FIN, SWE, CAN)",
        default="FIN"
    )

    season = Prompt.ask(
        "Enter season (e.g. 2024-25)",
        default="2024-25"
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    players = reader.get_players()

    stats = PlayerStats(players)
    selected_players = stats.top_scorers_by_nationality(
        nationality.upper()
    )

    table = Table(title=f"NHL players: {nationality.upper()} ({season})")

    table.add_column("Player")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in selected_players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            str(player.goals),
            str(player.assists),
            str(points)
        )

    console.print(table)


if __name__ == "__main__":
    main()
