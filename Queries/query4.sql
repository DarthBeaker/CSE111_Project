--Per player how many seasons played


SELECT p.p_player_firstname as Firstname, p.p_player_lastname as Lastname,
COUNT(DISTINCT pf_season_key) as Total_seasons
FROM players p
JOIN played_for pf ON pf.pf_player_key = p.p_player_key
GROUP BY p.p_player_firstname
ORDER By p.p_player_key;