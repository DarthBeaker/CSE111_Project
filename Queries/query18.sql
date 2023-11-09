/*
18 which player played the longest
*/


SELECT (players.p_player_firstname|| ' ' || players.p_player_lastname) as player, count(played_for.pf_season_key)
FROM players
JOIN played_for ON played_for.pf_player_key = players.p_player_key
GROUP BY player
HAVING count(played_for.pf_season_key) = 
(SELECT max(cnt) FROM (SELECT count(played_for.pf_season_key) as cnt FROM played_for GROUP BY played_for.pf_player_key))