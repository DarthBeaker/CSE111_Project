--Per season how many games


SELECT COUNT(*) as total_games, s.se_season_year as Season
FROM seasons s
JOIN games g ON g.g_season_key = s.se_season_key
