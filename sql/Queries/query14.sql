/*
14 coaches win rate
*/




SELECT coaches.c_coach_firstname as coach , round(count(game_win.winner_team_key),4)/(game_total.games_played) * 100 as winrate
FROM teams,(
    SELECT (CASE WHEN team_scores.home_score > team_scores.away_score THEN team_scores.home ELSE team_scores.away END) as winner_team_key
    FROM (
        SELECT substr(games.g_score,1,instr(games.g_score,'-')-1) as home_score, substr(games.g_score,instr(games.g_score,'-')+1) as away_score,
        games.g_team_key_away as away, games.g_team_key_home as home
        FROM games
    ) AS team_scores
) AS game_win,(
    SELECT teams.t_team_key as teamkey, 
    count(CASE WHEN teams.t_team_key = games.g_team_key_away OR teams.t_team_key = games.g_team_key_home THEN 1.0 ELSE 0.0 END) as games_played
    FROM teams
    JOIN games ON (teams.t_team_key = games.g_team_key_away OR teams.t_team_key = games.g_team_key_home)
    GROUP BY teams.t_team_key
) AS game_total
JOIN coaches ON coaches.c_coach_key = teams.t_coach_key 
WHERE teams.t_team_key = game_win.winner_team_key AND teams.t_team_key = game_total.teamkey
GROUP BY coaches.c_coach_key
