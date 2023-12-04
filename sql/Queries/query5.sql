--per team look up their players, coaches, mascots


SELECT t.t_team_name as Team, p.p_player_key as Player_key,
c.c_coach_key as Coaches, m.m_mascot_key as Mascot
FROM teams t
JOIN played_for pf ON pf.pf_team_key = t.t_team_key
JOIN coaches c ON c.c_coach_key = t.t_coach_key
JOIN players p ON p.p_player_key = pf.pf_player_key
JOIN mascots m ON m.m_mascot_key = t.t_mascot_key;
