/*
16 team win rate, overall seasons
*/


SELECT teams.t_team_name, round(game_win.cnt, 2)/game_total.games_played as winrate
FROM(
    SELECT game_win.winner_team_key, count(game_win.winner_team_key) as cnt
    FROM (
        SELECT (CASE WHEN ( cast(team_scores.home_score AS INT) > cast(team_scores.away_score AS INT) ) THEN team_scores.home ELSE team_scores.away END) as winner_team_key
        FROM (
            SELECT substr(games.g_score,1,instr(games.g_score,'-')-1) as home_score, substr(games.g_score,instr(games.g_score,'-')+1) as away_score,
            games.g_team_key_away as away, games.g_team_key_home as home
            FROM games
            ) AS team_scores
        ) AS game_win
        GROUP BY game_win.winner_team_key
    ) AS game_win,
    (
        SELECT teams.t_team_key as teamkey,
        count(CASE WHEN teams.t_team_key = games.g_team_key_away OR teams.t_team_key = games.g_team_key_home THEN 1.0 ELSE 0.0 END) as games_played
        FROM teams
        JOIN games ON (teams.t_team_key = games.g_team_key_away OR teams.t_team_key = games.g_team_key_home)
        GROUP BY teams.t_team_key
    ) AS game_total
JOIN teams ON teams.t_team_key = game_total.teamkey
WHERE game_win.winner_team_key = game_total.teamkey
GROUP BY game_total.teamkey