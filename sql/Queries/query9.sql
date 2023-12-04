--win count of teams


SELECT
  t.t_team_name as Team,
  SUM(CASE
    WHEN t.t_team_key = g.g_team_key_home AND CAST(substr(g.g_score, 1, instr(g.g_score, '-') - 1) AS INTEGER) > CAST(substr(g.g_score, instr(g.g_score, '-') + 1) AS INTEGER) THEN 1
    WHEN t.t_team_key = g.g_team_key_away AND CAST(substr(g.g_score, 1, instr(g.g_score, '-') - 1) AS INTEGER) < CAST(substr(g.g_score, instr(g.g_score, '-') + 1) AS INTEGER) THEN 1
    ELSE 0
  END) AS Total_wins
FROM teams t
JOIN played_for pf ON t.t_team_key = pf.pf_team_key
JOIN games g ON pf.pf_season_key = g.g_season_key
GROUP BY Team;