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
const fetchPromises = [];
const jsonPromises = [];

function addFactsToList(list, factsJSON) {
  if (factsJSON === undefined) {
    let error = document.createElement("li");
    error.textContent = "Something went wrong getting this fact.";
    list.append(error);
  } else if (factsJSON.text) {
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

async function jsonFromFetches() {
  let resolved = await Promise.allSettled(fetchPromises);
  resolved.forEach((resp) => {
    jsonPromises.push(resp.value.json());
  });
}

async function displayJSONResults() {
  let facts = await Promise.allSettled(jsonPromises);
  addFactsToList(singleFact, facts[0].value);
  addFactsToList(multFactDiff, facts[1].value);
  facts.slice(2).forEach((fact) => addFactsToList(multFactSame, fact.value));
}

async function getFacts() {
  fetchPromises.push(fetch(NUMBER_URL + "29?json"));
  fetchPromises.push(fetch(NUMBER_URL + "9,29,929?json"));
  for (let x = 0; x < 4; x++) {
    fetchPromises.push(fetch(NUMBER_URL + "29?json"));
  }
  try {
    await jsonFromFetches();
  } catch (error) {
    console.log("Error in getting facts");
    console.error(error);
  }
  try {
    await displayJSONResults();
  } catch (error) {
    console.log("Error in parsing JSON");
    console.error(error);
  }
}

getFacts();
