class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.scores = []

    def AddPlayer(self, player_name):
        self.players.append(player_name)
        print(f"Player {player_name} connect to {self.name}")

    def ReplacePlayer(self,old_player, new_player):
        if old_player in self.players:
            index = self.players.index(old_player)
            self.players[index] = new_player
            print(f"Player {old_player} is replaced {new_player} in the {self.name}")

    def RemovePlayer(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            print(f"Player {player_name} was removed from {self.name}")
        else:
            print(f"Player {player_name} didnt found in {self.name}")

    def AddScores(self, score):
        self.scores.append(score)
        print(f"Team {self.name} gets {score} points")

    def display(self):
        print(f"Team {self.name}")
        print("Players: " + '', '',''.join(self.players))
        print(f"Point by tournament:" + '', '', ''.join(map(str, self.scores)))
        print(f"General numbers of point: {sum(self.scores)}")

team1 = Team("GGG")
team2 = Team("AAA")

team1.AddPlayer("Dasha")
team1.AddPlayer("Kate")
team1.AddPlayer("Sasha")

team2.AddPlayer("Anton")
team2.AddPlayer("Liza")
team2.AddPlayer("Misha")

team1.AddScores(3)
team1.AddScores(4)
team1.AddScores(7)

team2.AddScores(6)
team2.AddScores(9)
team2.AddScores(2)

team1.display()
team2.display()

team1.RemovePlayer("Dasha")
team1.AddPlayer("Vlad")