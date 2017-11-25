n = int(input())
teams = dict()

#0 всего игр - 1 побед - 2 ничьих - 3 поражений - 4 всего очков
for i in range(n):
    team1, score1, team2, score2 = input().split(';')

    if team1 not in teams.keys():
        teams[team1] = [0, 0, 0, 0, 0]
    if team2 not in teams.keys():
        teams[team2] = [0, 0, 0, 0, 0]

    teams[team1][0] += 1
    teams[team2][0] += 1

    if score1 > score2:
        teams[team1][1] += 1
        teams[team1][4] += 3
        teams[team2][3] += 1
    elif score1 < score2:
        teams[team2][1] += 1
        teams[team2][4] += 3
        teams[team1][3] += 1
    elif score1 == score2:
        teams[team1][2] += 1
        teams[team1][4] += 1
        teams[team2][2] += 1
        teams[team2][4] += 1

for key, value in teams.items():
    print(key, end=':')

    for v in value:
        print(v, end=' ')

    print()
