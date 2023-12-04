--all games coaches coached for


SELECT c_coach_firstname as Firstname, c_coach_lastname as Lastname,
g_game_key as Game_key
FROM coaches
JOIN teams ON t_coach_key = c_coach_key
JOIN games ON t_team_key = g_team_key_home OR t_team_key = g_team_key_away;