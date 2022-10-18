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
      })
      .catch((error) => {
        cardHolder.textContent = "Something went wrong while drawing a card.";
        console.error(error);
      });
  }
  if (deck.remaining === 0) {
    cardHolder.textContent = "No Cards Left!";
    cardHolder.setAttribute("enabled", false);
  }
}

function displayCard(cardObj) {
  let cardElement = document.createElement("img");
  cardElement.setAttribute("src", cardObj.image);
  cardHolder.append(cardElement);
}

drawButton.addEventListener("click", drawCard);
