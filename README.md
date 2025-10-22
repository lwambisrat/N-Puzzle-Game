# N-Puzzle Game Solver

This project is a smart A* search engine, built simply in Python, that cracks the N-Puzzle. It works by letting you type in your scrambled board configuration, after which the program instantly runs a solvability check to save you time on impossible layouts. If the puzzle is valid, it uses the efficient Manhattan distance heuristic to guarantee the absolute shortest path to the solution.



## Table of Contents

- Features
- Requirements
- Clone the repository
- Run the solver
- Input format and example
- How the solver works
- Google Colab demo to test the functionality
- Troubleshooting


---


## Features

- Solvability check for general N-Puzzle sizes (e.g., 8-puzzle, 15-puzzle).
- A* search with Manhattan distance heuristic.
- Human-friendly interactive input (console prompts).
- Prints the optimal path length and sequence of moves when a solution is found.

---

## Requirements

- Python version 3 or above

---

## Clone the repository

Using SSH:
```
git clone git@github.com:lwambisrat/N-Puzzle-Game.git
cd N-Puzzle-Game
```

Or using HTTPS:
```
git clone https://github.com/lwambisrat/N-Puzzle-Game.git
cd N-Puzzle-Game
```

---

## Run the solver

To start solving, just open your terminal in the repository folder and run the main script using Python:
```
python3 n_puzzle_solver.py
```

The script will run interactively and prompt for:
- Number of blocks N (e.g., 8 for 3x3 puzzle, 15 for 4x4)
- Starting index for the empty tile (0)
- The remaining N tile numbers (1..N) in a single line separated by spaces

## Input format and example

Example: solve the 8-puzzle (3x3)

When prompted:
- Enter the number of blocks (N) [e.g., 8, 15]: 8

- Enter the STARTING index for the empty block (0) (0 to 8): 4  
  (Indices are 0-based, left-to-right, top-to-bottom; index 4 is the center of a 3x3)

- Enter the 8 remaining tiles (1 to 8), separated by spaces:  
  1 2 3 4 5 6 7 8

The program will assemble the full layout by inserting 0 at the chosen position:
[1, 2, 3, 4, 0, 5, 6, 7, 8]

Expected behavior:
- The program prints the board, checks solvability, runs A* if solvable, then prints the optimal path length and sequence of moves (Up, Down, Left, Right).

Sample interactive session (abbreviated):
```
Enter the number of blocks (N) [e.g., 8, 15]: 8
Enter the STARTING index for the empty block (0) (0 to 8): 4
Remaining Tiles (separated by spaces): 1 2 3 4 5 6 7 8

System Assembled Initial Layout: [1, 2, 3, 4, 0, 5, 6, 7, 8]
3x3 N-Puzzle Solver--->
Initial State:
(1, 2, 3)
(4, 0, 5)
(6, 7, 8)

Solvability Check: it is SOLVABLE-> because the rule is fulfilled

Running A* Search for Optimal Path...
Solution Found --->
Optimal Path Length (G-score): X
Sequence of Moves that you need to follow:
Up
Left
...
```

---

## How the solver works

- Board representation: the board is represented as a tuple of tuples (immutable), with `0` representing the blank tile.
- Goal state: the tiles are arranged in increasing order with `0` at the last position.
- Solvability check:
  - Computes inversions on the flattened tile list (excluding 0).
  - For odd board width, puzzle is solvable if inversions parity is even.
  - For even board width, uses the blank row from bottom parity rule.
- A* search:
  - Uses a priority queue (`heapq`) with entries (f, g, board, path) where f = g + h.
  - Heuristic h is Manhattan distance: sum of distances of each tile from its goal position.
  - Explores neighbors by sliding the blank up/down/left/right.
  - Tracks `g_scores` to avoid revisiting worse paths.

---

## Google Colab demo to Test the functionality

Try out the solver. Open the interactive Colab notebook for a fun visual experience. It includes a clickable grid interface so you can easily test board configurations and watch the results.

Open the Colab test here:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17Lkjzn3T9rwCbEeLngqkUtWSJZA1ZPk4)

What the Colab test does
- Runs an interactive widget-based N-Puzzle within Colab.
- Performs solvability analysis and prints an explanation.
- Allows clicking adjacent tiles to move them - shows move count and success message when the puzzle is solved.
- Uses ipywidgets for the UI - input() is used for initial layout in the current notebook version but the main interaction is widget-based.

How to run the Colab test

1.Hit the "Open In Colab" link to jump straight to the notebook.

2.Once it's loaded, select Runtime → Run all from the menu to execute the code.

3.The notebook will ask you for a few things—just enter the puzzle size and the tile layout when prompted (there are examples to guide you!).

4.A clickable grid will appear! Use it to play with the puzzle and see the solver's logic in real-time.


## Troubleshooting

- If the program reports the puzzle as unsolvable, re-check the tile permutation and blank position
- If you see no solution for a puzzle that should be solvable, ensure you entered tiles in the correct order and the blank index is correct (0-based).
- If runtime/memory usage is excessive for larger puzzles (e.g., 24-puzzle), consider switching to IDA* or using a specialized solver.







