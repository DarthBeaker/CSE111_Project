//fetch request that posts
const insert_into_table_player = (player_key, player_firstname, player_lastname, player_age, team_name, salary, season_year) => {
    return fetch("/insert_into_players", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({player_key, player_firstname, player_lastname, player_age, team_name, salary, season_year})
    }).then(res => res.json())
    .then(res => {
        if (res.okay) {
            alert("Data Inserted into Table Players");
        } 
        else if(res.error) {
            alert(`Failed to Insert Data: ${res.error}`);
        }
    });
}


const insert_into_players = () => {

    const player_key_elem = document.querySelector("#p-player-key");
    const player_firstname_elem = document.querySelector("#p-player-firstname");
    const player_lastname_elem = document.querySelector("#p-player-lastname");
    const player_age_elem = document.querySelector("#p-player-age");
    const team_name_elem = document.querySelector("#t-team-name");
    const salary_elem = document.querySelector("#pf-salary");
    const season_year_elem = document.querySelector("#se-season-year");

    const player_key = player_key_elem.value;
    const player_firstname = player_firstname_elem.value;
    const player_lastname = player_lastname_elem.value;
    const player_age = player_age_elem.value;
    const team_name = team_name_elem.value;
    const salary = salary_elem.value;
    const season_year = season_year_elem.value;

    insert_into_table_player(player_key, player_firstname, player_lastname, player_age, team_name, salary, season_year); 
}