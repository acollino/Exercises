const drawButton = document.querySelector("#draw-btn");
const cardHolder = document.querySelector("#card-holder");
const ERROR_URL = "/async/async_await/error_card.jpg";
const deck = {};

async function getDeck() {
  try {
    let resp = await fetch(
      "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    );
    let respJSON = await resp.json();
    deck.id = respJSON.deck_id;
    deck.remaining = respJSON.remaining;
  } catch (error) {
    cardHolder.textContent = "Something went wrong while requesting the deck.";
    console.error(error);
  }
}

async function drawCard() {
  if (deck.remaining > 0) {
    try {
      let cardResp = await fetch(
        `https://deckofcardsapi.com/api/deck/${deck.id}/draw/?count=1`
      );
      let cardJSON = await cardResp.json();
      displayCard(cardJSON.cards[0]);
      deck.remaining = cardJSON.remaining;
      if (deck.remaining === 0) {
        drawButton.textContent = "No Cards Left!";
        drawButton.setAttribute("disabled", true);
      }
    } catch (error) {
      console.log("safely caught");
      displayCard({ image: ERROR_URL });
      console.error(error);
    }
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

getDeck();
drawButton.addEventListener("click", drawCard);
