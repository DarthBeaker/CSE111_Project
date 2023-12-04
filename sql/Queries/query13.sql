/*
13 last game per season, team that won
*/

.headers ON

SELECT finalgame.season as season, teams.t_team_name as final_match_winner
FROM teams, (
    SELECT (CASE WHEN final_team_scores.home_score > final_team_scores.away_score THEN final_team_scores.home ELSE final_team_scores.away END) as winner_team_key, 
    final_team_scores.season as season
    FROM (
        SELECT substr(games.g_score,1,instr(games.g_score,'-')-1) as home_score, substr(games.g_score,instr(games.g_score,'-')+1) as away_score, seasons.se_season_year as season,
        games.g_team_key_away as away, games.g_team_key_home as home
        FROM games
        JOIN seasons ON seasons.se_season_key = games.g_season_key
        WHERE games.g_date IN (SELECT max(games.g_date) FROM games GROUP BY games.g_season_key)
    ) AS final_team_scores
) AS finalgame
WHERE teams.t_team_key = finalgame.winner_team_key