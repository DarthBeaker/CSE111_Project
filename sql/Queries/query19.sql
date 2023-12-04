/*
19 print all games per stadium
*/

SELECT stadiums.s_name as stadium_name, (hometeam.t_team_name|| ' vs ' || awayteam.t_team_name) as match_up
FROM games
JOIN stadiums ON games.g_stadium_key = stadiums.s_stadium_key
JOIN teams as hometeam ON hometeam.t_team_key = games.g_team_key_home
JOIN teams as awayteam ON awayteam.t_team_key = games.g_team_key_away
GROUP BY stadiums.s_stadium_key, match_up;