--Join played_for with players, teams, and seasons


SELECT * FROM played_for
JOIN players ON pf_player_key = p_player_key
JOIN teams ON pf_team_key = t_team_key
JOIN seasons ON pf_season_key = se_season_key;