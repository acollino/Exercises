const drawButton = document.querySelector("#draw-btn");
const cardHolder = document.querySelector("#card-holder");
const deck = {};

fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
  .then((resp) => resp.json())
  .then((respJSON) => {
    deck.id = respJSON.deck_id;
    deck.remaining = respJSON.remaining;
  })
  .catch((error) => {
    cardHolder.textContent = "Something went wrong while requesting the deck.";
    console.error(error);
  });

function drawCard() {
  if (deck.remaining > 0) {
    fetch(`https://deckofcardsapi.com/api/deck/${deck.id}/draw/?count=1`)
      .then((resp) => resp.json())
      .then((respJSON) => {
        displayCard(respJSON.cards[0]);
        deck.remaining = respJSON.remaining;
        if (deck.remaining === 0) {
          drawButton.textContent = "No Cards Left!";
          drawButton.setAttribute("disabled", true);
        }
      })
      .catch((error) => {
        console.log("Something went wrong while drawing a card.");
        console.error(error);
      });
  }
}

// Random angle is between -45 and 45deg
// Random X,Y are between -2 and ~2
function displayCard(cardObj) {
  let cardElement = document.createElement("img");
  cardElement.setAttribute("src", cardObj.image);
  cardElement.classList.add("card");
  let randomAngle = Math.floor(Math.random() * 91 - 45);
  let randomY = Math.random() * 4 - 2;
  let randomX = Math.random() * 4 - 2;
  cardElement.style.transform = `rotate(${randomAngle}deg) translateX(${randomX}rem) translateY(${randomY}rem)`;
  cardHolder.append(cardElement);
}

drawButton.addEventListener("click", drawCard);
