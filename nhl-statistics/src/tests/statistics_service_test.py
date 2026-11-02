import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_returns_players_from_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")

    def test_team_returns_empty_list_if_team_not_found(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )
    def test_top_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux"]
        )

    def test_top_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman"]
        )

    def test_top_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman"]
        )


if __name__ == "__main__":
    unittest.main()
