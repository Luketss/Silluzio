function fibonacci(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

function fibonacciSequence(m, n) {
    const max = Math.max(m, n);
    let i = 0;
    while (fibonacci(i) <= max) {
        console.log(fibonacci(i));
        i++;
    }
}

const value1 = parseInt(prompt("Digite o primeiro valor:"));
const value2 = parseInt(prompt("Digite o segundo valor:"));

fibonacciSequence(value1, value2);



//------------------------------------------------------------------------------------------------------------------

function countRepeatedLetters(name) {
    const nameWithoutFirstLetter = name.slice(1);
    const letterCount = {};

    for (let i = 0; i < nameWithoutFirstLetter.length; i++) {
        const letter = nameWithoutFirstLetter[i];
        if (letterCount[letter]) {
            letterCount[letter]++;
        } else {
            letterCount[letter] = 1;
        }
    }

    return letterCount;
}

const nome = prompt("Digite um nome:").toLowerCase(); // Convertendo o nome para minúsculas para considerar letras maiúsculas e minúsculas como iguais
const letterCounts = countRepeatedLetters(nome);

for (const letter in letterCounts) {
    if (letterCounts[letter] > 1) {
        console.log(`A letra "${letter}" se repete ${letterCounts[letter]} vezes.`);
    }
}


//------------------------------------------------------------------------------------------------------------------

function printBoard(board) {
    for (let i = 0; i < 4; i++) {
        console.log(board[i].join(" "));
    }
}

function isSafe(board, row, col, num) {
    for (let x = 0; x < 4; x++) {
        if (board[row][x] === num || board[x][col] === num) {
            return false;
        }
    }

    const startRow = row - (row % 2);
    const startCol = col - (col % 2);
    for (let i = startRow; i < startRow + 2; i++) {
        for (let j = startCol; j < startCol + 2; j++) {
            if (board[i][j] === num) {
                return false;
            }
        }
    }

    return true;
}

function solveSudoku(board, row, col) {
    if (row === 4 - 1 && col === 4) {
        return true;
    }

    if (col === 4) {
        row++;
        col = 0;
    }

    if (board[row][col] !== 0) {
        return solveSudoku(board, row, col + 1);
    }

    for (let num = 1; num <= 4; num++) {
        if (isSafe(board, row, col, num)) {
            board[row][col] = num;
            if (solveSudoku(board, row, col + 1)) {
                return true;
            }
            board[row][col] = 0;
        }
    }

    return false;
}

function generateSudoku() {
    const board = Array.from({ length: 4 }, () => Array(4).fill(0));

    if (solveSudoku(board, 0, 0)) {
        printBoard(board);
    } else {
        console.log("Não foi possível gerar um quadro de Sudoku válido.");
    }
}

generateSudoku();
