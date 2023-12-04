/*
20 top paid players
*/

SELECT (players.p_player_firstname|| ' ' || players.p_player_lastname) as player, played_for.pf_salary as salary
FROM players
JOIN played_for ON played_for.pf_player_key = players.p_player_key
WHERE played_for.pf_salary = (SELECT max(played_for.pf_salary) FROM played_for)