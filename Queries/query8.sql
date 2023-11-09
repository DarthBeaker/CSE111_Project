--total number of players in a season

SELECT se_season_year as Season, COUNT(DISTINCT pf_player_key) as Total_players
FROM seasons
JOIN played_for ON pf_season_key = se_season_key
GROUP BY Season;