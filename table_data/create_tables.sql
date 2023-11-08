CREATE TABLE players (
    p_player_key decimal(3,0) not null,
    p_player_firstname varchar(25) not null,
    p_player_lastname varchar(25) not null,
    p_player_age decimal(3,0) not null
);
CREATE TABLE teams (
    t_team_key decimal(3,0) not null,
    t_mascot_key decimal(3,0) not null,
    t_coach_key decimal(3,0) not null,
    t_team_name varchar(25) not null
);
CREATE TABLE played_for (
    pf_player_key decimal(3,0) not null,
    pf_team_key decimal(3,0) not null,
    pf_season_key decimal(3,0) not null,
    pf_salary decimal(11,0) not null
);
CREATE TABLE seasons (
    se_season_key decimal(3,0) not null,
    se_season_year date not null
);
CREATE TABLE games(
    g_game_key decimal(3,0) not null,
    g_team_key_home decimal(3,0) not null,
    g_team_key_away decimal(3,0) not null,
    g_stadium_key decimal(3,0) not null,
    g_season_key decimal(3,0) not null,
    g_score varchar(10) not null
);
CREATE TABLE stadiums (
    s_stadium_key decimal(3,0) not null,
    s_name varchar(25) not null
);
CREATE TABLE mascots (
    m_mascot_key decimal(3,0) not null,
    m_name varchar(25) not null
);
CREATE TABLE coaches (
    c_coach_key decimal(3,0) not null,
    c_coach_firstname varchar(25) not null,
    c_coach_lastname varchar(25) not null,
    c_coach_age decimal(3,0) not null
);
