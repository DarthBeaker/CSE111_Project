/*
11 how many games per stadium per season
*/


SELECT stadiums.s_name as stadium_name, seasons.se_season_year as season, count(games.g_game_key) as cnt
FROM games
JOIN stadiums ON games.g_stadium_key = stadiums.s_stadium_key
JOIN seasons ON seasons.se_season_key = games.g_season_key
GROUP BY seasons.se_season_key, stadiums.s_stadium_key;