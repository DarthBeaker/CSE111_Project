/*
12 which stadium played the most during season
*/



SELECT stadiums.s_name as stadium_name, seasons.se_season_year as season
FROM stadiums, (
    SELECT max(stadium_played.count) as cnt
    FROM (
        SELECT count(games.g_game_key) as count
        FROM games
        GROUP BY games.g_season_key, games.g_stadium_key
    )stadium_played
)max_cnt
JOIN games ON games.g_stadium_key = stadiums.s_stadium_key
JOIN seasons ON seasons.se_season_key = games.g_season_key
GROUP BY games.g_season_key, games.g_stadium_key
HAVING count(games.g_game_key) = max_cnt.cnt;