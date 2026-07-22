![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🎰 Fruit Machine

A Python solution to the Codewars kata **"Fruit Machine"**.


## ⁉ Problem

Simulate the scoring system of a three-reel fruit machine (slot machine).

Each reel contains a list of symbols, and the position where each reel stops is provided. Based on the combination of symbols shown, calculate the player's score.


### Scoring Rules

- Three matching symbols → **symbol value × 10**
- Two matching symbols + one **Wild** → **symbol value × 2**
- Two **Wilds** + one different symbol → **10 points**
- Two matching symbols (without a Wild) → **symbol value**
- No matching symbols → **0 points**


### Symbol Values

| Symbol | Value |
|--------|------:|
| Wild | 10 |
| Star | 9 |
| Bell | 8 |
| Shell | 7 |
| Seven | 6 |
| Cherry | 5 |
| Bar | 4 |
| King | 3 |
| Queen | 2 |
| Jack | 1 |


## Approach

The solution:

1. Determines the symbol shown on each reel using the given spin positions.
2. Counts how many unique symbols appear.
3. Applies the scoring rules based on the combination rolled.
4. Returns the corresponding score.
