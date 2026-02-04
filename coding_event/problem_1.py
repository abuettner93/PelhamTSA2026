teams = [("Team A", 1),
         ("Team B", 3),
         ("Team C", 2),
         ("Team D", 4),
         ("Team E", 5),
         ("Team F", 6)
         ]

# when using a list, the order MATTERS
scoring = [10, 7, 5, 2]

scoring_dict = {1: 10,
                3: 5,
                2: 7,
                4: 2}



teams_and_points = []
for team in teams:
    team_name, placement = team
    if placement > 4:
        points = 0
    else:
        points = scoring_dict[placement]
    scored_team = (team_name, placement, points)
    teams_and_points.append(scored_team)
    # print(f"Team: {team_name}, Placement: {placement}, Points: {points}")

sorted_descending = sorted(teams_and_points, reverse=True, key=lambda x: x[2])  # , key=lambda x: x[1], reverse=True)
print(sorted_descending)
