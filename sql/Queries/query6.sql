--all games in a season

SELECT se_season_year as Season, g_game_key as Game_key
FROM seasons
JOIN games ON g_season_key = se_season_key;