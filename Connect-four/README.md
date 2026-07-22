![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🔴🟡 Connect Four

A Python solution to the Codewars kata **"Connect Four - Who Won?"**.


## ⁉ Problem

Simulate a game of **Connect Four** and determine the winner.

The game is played on a **6 × 7** grid. Players take turns dropping colored pieces into one of the seven columns. Each piece falls to the lowest available position in its column.

The input is a list of moves in the format:

```text
Column_Color
```

For example:

```text
A_Red
C_Yellow
G_Red
```

The task is to determine which player wins by connecting **four consecutive pieces**:

- Horizontally
- Vertically
- Diagonally

If neither player wins after all moves have been played, return `"Draw"`.


## Approach

The solution:

1. Represents the game board as a 6 × 7 matrix.
2. Converts the input into column indices and player identifiers.
3. Simulates each move by placing the piece in the lowest available row.
4. After every move, checks for four consecutive matching pieces in all directions.
5. Returns the winner immediately when a winning sequence is found.
