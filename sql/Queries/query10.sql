--AVG score for teams

SELECT
  t.t_team_name AS Team,
  AVG(team_scores.Score) AS Average_Score
FROM teams t
JOIN played_for pf ON t.t_team_key = pf.pf_team_key
LEFT JOIN (
  SELECT
    g.g_team_key_home AS TeamKey,
    CAST(substr(g.g_score, 1, instr(g.g_score, '-') - 1) AS INTEGER) AS Score
  FROM games g
  UNION ALL
  SELECT
    g.g_team_key_away AS TeamKey,
    CAST(substr(g.g_score, instr(g.g_score, '-') + 1) AS INTEGER) AS Score
  FROM games g
) AS team_scores ON t.t_team_key = team_scores.TeamKey
GROUP BY Team;