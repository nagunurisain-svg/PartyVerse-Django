const playerInput = document.getElementById("playerInput");
const addPlayerButton = document.getElementById("addPlayer");
const playersList = document.getElementById("playersList");
const emptyMessage = document.getElementById("emptyMessage");
const continueButton = document.getElementById("continueButton");

let players = [];

function addPlayer() {

    const name = playerInput.value.trim();

    if (name === "") {
        alert("Please enter a player name.");
        return;
    }

    if (players.length >= 12) {
        alert("Maximum 12 players allowed.");
        return;
    }

    if (players.some(player => player.toLowerCase() === name.toLowerCase())) {
        alert("This player is already added.");
        playerInput.value = "";
        return;
    }

    players.push(name);

    playerInput.value = "";

    displayPlayers();

    playerInput.focus();
}


function displayPlayers() {

    playersList.innerHTML = "";

    if (players.length === 0) {

        emptyMessage.style.display = "block";

    } else {

        emptyMessage.style.display = "none";

    }


    players.forEach((player, index) => {

        const playerCard = document.createElement("div");

        playerCard.className = "player-card";

        playerCard.innerHTML = `
            <div class="player-info">

                <div class="player-number">
                    ${index + 1}
                </div>

                <div class="player-name">
                    ${player}
                </div>

            </div>

            <button
                class="remove-player"
                type="button"
                onclick="removePlayer(${index})">
                ×
            </button>
        `;

        playersList.appendChild(playerCard);

    });


    if (players.length >= 2) {

        continueButton.disabled = false;

    } else {

        continueButton.disabled = true;

    }
}


function removePlayer(index) {

    players.splice(index, 1);

    displayPlayers();
}


addPlayerButton.addEventListener("click", function () {

    addPlayer();

});


playerInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        addPlayer();

    }

});