//ES5 Map Callback
function double(arr) {
  return arr.map(function(val) {
    return val * 2;
  });
}

/*ES2015 Arrow Functions Shorthand
Refactor the above code to use two arrow functions. Turn it into a one-liner.*/
const doubleArrow = arr => arr.map(val => val * 2);

//Replace ALL functions with arrow functions:
function squareAndFindEvens(numbers){
  var squares = numbers.map(function(num){
    return num ** 2;
  });
  var evens = squares.filter(function(square){
    return square % 2 === 0;
  });
  return evens;
}

const squareAndFindEvensArrow = numbers => {
  return numbers.map(num => num ** 2).filter(square => square % 2 === 0);
};
//could have done this in one line as well
//no need for parentheses around the parameter - would need for 0 or 2+ parameters though