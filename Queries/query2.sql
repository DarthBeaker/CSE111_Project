--Per season how many games
--currently only have games for 2019&2020


SELECT COUNT(DISTINCT g.g_game_key) as total_games, s.se_season_year as Season
FROM seasons s
JOIN games g ON g.g_season_key = s.se_season_key
Group BY s.se_season_year;