/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

class Game {
  constructor(width = 7, height = 6) {
    this.width = width;
    this.height = height;
    this.board = [];
    this.player1 = new Player("#ff0000").setNumber(1);
    this.player2 = new Player("#0000ff").setNumber(2);
    this.currPlayer = this.player1;
    this.gameOver = false;
  }

  makeBoard() {
    for (let y = 0; y < this.height; y++) {
      this.board.push(Array.from({ length: this.width }));
    }
  }

  makeHtmlBoard() {
    const board = document.getElementById("board");
    const top = document.createElement("tr");
    top.setAttribute("id", "column-top");
    top.addEventListener("click", this.handleClick.bind(this));

    for (let x = 0; x < this.width; x++) {
      const headCell = document.createElement("td");
      headCell.setAttribute("id", x);
      top.append(headCell);
    }

    board.append(top);

    for (let y = 0; y < this.height; y++) {
      const row = document.createElement("tr");

      for (let x = 0; x < this.width; x++) {
        const cell = document.createElement("td");
        cell.setAttribute("id", `${y}-${x}`);
        row.append(cell);
      }

      board.append(row);
    }
  }

  findSpotForCol(x) {
    for (let y = this.height - 1; y >= 0; y--) {
      if (!this.board[y][x]) {
        return y;
      }
    }
    return null;
  }

  placeInTable(y, x) {
    const piece = document.createElement("div");
    piece.classList.add("piece");
    piece.style.backgroundColor = this.currPlayer.color;
    piece.style.top = -50 * (y + 2);

    const spot = document.getElementById(`${y}-${x}`);
    spot.append(piece);
  }

  endGame(msg) {
    this.gameOver = true;
    alert(msg);
  }

  handleClick(evt) {
    if (this.gameOver) {
      return;
    }
    const x = +evt.target.id;
    const y = this.findSpotForCol(x);
    if (y === null || isNaN(x)) {
      return;
    }

    this.board[y][x] = this.currPlayer;
    this.placeInTable(y, x);

    if (this.checkForWin()) {
      return this.endGame(`Player ${this.currPlayer.number} won!`);
    }

    if (this.board.every((row) => row.every((cell) => cell))) {
      return this.endGame("Tie!");
    }

    this.currPlayer =
      this.currPlayer === this.player1 ? this.player2 : this.player1;
  }

  checkForWin() {
    const _win = (cells) => {
      return cells.every(
        ([y, x]) =>
          y >= 0 &&
          y < this.height &&
          x >= 0 &&
          x < this.width &&
          this.board[y][x] === this.currPlayer
      );
    };

    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        const horiz = [
          [y, x],
          [y, x + 1],
          [y, x + 2],
          [y, x + 3],
        ];
        const vert = [
          [y, x],
          [y + 1, x],
          [y + 2, x],
          [y + 3, x],
        ];
        const diagDR = [
          [y, x],
          [y + 1, x + 1],
          [y + 2, x + 2],
          [y + 3, x + 3],
        ];
        const diagDL = [
          [y, x],
          [y + 1, x - 1],
          [y + 2, x - 2],
          [y + 3, x - 3],
        ];

        if (_win(horiz) || _win(vert) || _win(diagDR) || _win(diagDL)) {
          return true;
        }
      }
    }
  }

  deletePieces() {
    let pieceList = document.querySelectorAll(".piece");
    pieceList.forEach((piece) => piece.remove());
  }

  startGame() {
    if (document.getElementById("column-top")) {
      return this.resetGame();
    }
    this.makeBoard();
    this.makeHtmlBoard();
  }

  resetGame() {
    this.currPlayer = this.player1;
    this.board = [];
    this.makeBoard();
    this.deletePieces();
    this.gameOver = false;
  }
}

class Player {
  constructor(color) {
    this.color = color;
  }

  setNumber(num) {
    this.number = num;
    return this;
  }

  setColor(stringColor) {
    this.color = stringColor;
  }
}

let game = new Game(7, 6);

const resetButton = document.querySelector("#play-button");
resetButton.addEventListener("click", game.startGame.bind(game));

const p1ColorInput = document.querySelector("#p1-color");
const p2ColorInput = document.querySelector("#p2-color");
const colorSubmit = document.querySelector("#color-submit");
colorSubmit.addEventListener("click", function (evt) {
  evt.preventDefault();
  if (colorWarningCheck()) {
    let choice = confirm(
      `Warning: Changing a player's color mid-game can be confusing.
                Proceed anyway?`
    );
    if (!choice) {
      return;
    }
  }
  game.player1.setColor(p1ColorInput.value);
  game.player2.setColor(p2ColorInput.value);
});

function colorWarningCheck() {
  let piecePresent = Boolean(document.querySelector(".piece"));
  let gameInProgress = !game.gameOver;
  let p1Changed = p1ColorInput.value !== game.player1.color;
  let p2Changed = p2ColorInput.value !== game.player2.color;
  return piecePresent && gameInProgress && (p1Changed || p2Changed);
}
