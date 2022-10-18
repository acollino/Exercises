/**
 * Instructions:
 * Make a request to the Numbers API (http://numbersapi.com/) to get a fact
 * about your favorite number. (Make sure you get back JSON by including
 * the json query key, specific to this API.)
 *
 * Figure out how to get data on multiple numbers in a single request.
 * Make that request and when you get the data back, put all of the
 * number facts on the page.
 *
 * Use the API to get 4 facts on your favorite number.
 * Once you have them all, put them on the page.
 * It’s okay if some of the facts are repeats.
 */

const singleFact = document.querySelector("#single-fact");
const multFactDiff = document.querySelector("#multiple-facts-diff");
const multFactSame = document.querySelector("#multiple-facts-same");
const NUMBER_URL = "http://numbersapi.com/";

function addFactsToList(list, factsJSON) {
  if (factsJSON.text) {
    let fact = document.createElement("li");
    fact.textContent = factsJSON.text;
    list.append(fact);
  } else {
    for (let fact of Object.values(factsJSON)) {
      let factLI = document.createElement("li");
      factLI.textContent = fact;
      list.append(factLI);
    }
  }
}

function makeFactRequest(url, targetList, errorMsg) {
  return fetch(url)
    .then((resp) => resp.json())
    .then((respJson) => {
      addFactsToList(targetList, respJson);
    })
    .catch((error) => {
      singleFact.textContent = errorMsg;
      console.error(error);
    });
}

makeFactRequest(
  NUMBER_URL + "29?json",
  singleFact,
  "An error occurred while getting this fact."
);

makeFactRequest(
  NUMBER_URL + "9,29,929?json",
  multFactDiff,
  "An error occurred while getting these facts."
);

let promiseArray = [];

for (let x = 0; x < 4; x++) {
  promiseArray.push(
    makeFactRequest(
      NUMBER_URL + "29?json",
      multFactSame,
      "An error occurred while getting these facts."
    )
  );
}

Promise.all(promiseArray);
