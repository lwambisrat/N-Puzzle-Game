# N-Puzzle Game Solver

A simple A* solver for the N-Puzzle (sliding puzzle) implemented in Python.  
This repository contains a console program that accepts a user-provided board configuration, checks solvability, and—if solvable—searches for an optimal solution using the Manhattan distance heuristic.

Note: your main solver file is named `n_puzzle_solver.py`. The README below assumes that filename.

---

## Table of Contents

- Overview
- Features
- Requirements
- Clone the repository
- Run the solver
  - Recommended: n_puzzle_solver.py
- Input format and example
- How the solver works
- Complexity and limitations
- Troubleshooting
- Contributing
- License

---

## Overview

The N-Puzzle Game Solver reads a user-provided N-Puzzle initial layout, determines if the layout is solvable, and, if so, runs an A* search using the Manhattan distance heuristic to find an optimal sequence of moves from the initial board to the goal.

The goal board used by the solver is the canonical layout:
1 2 3 ...
... N 0

Where `0` denotes the empty tile.

---

## Features

- Solvability check for general N-Puzzle sizes (e.g., 8-puzzle, 15-puzzle).
- A* search with Manhattan distance heuristic.
- Human-friendly interactive input (console prompts).
- Prints the optimal path length and sequence of moves when a solution is found.

---

## Requirements

- Python 3.7+ (recommended: Python 3.8 or later)
- No external Python packages are required (uses only Python standard library: `heapq`, `math`).

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

This repository's solver script is `n_puzzle_solver.py`. Run it with Python:

```
python3 n_puzzle_solver.py
```

The script will run interactively and prompt for:
- Number of blocks N (e.g., 8 for 3x3 puzzle, 15 for 4x4)
- Starting index for the empty tile (0)
- The remaining N tile numbers (1..N) in a single line separated by spaces

Follow the prompts exactly. The program will assemble the full board internally.

---

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

## Complexity and limitations

- A* with Manhattan heuristic is admissible and typically effective for small N (8, 15).
- Memory usage grows quickly with branching factor — large puzzles (e.g., 24-puzzle) may be infeasible to solve optimally on a typical machine.
- Performance improvements to consider:
  - IDA* (Iterative Deepening A*) to limit memory usage.
  - More advanced heuristics (pattern databases) for larger puzzles.
  - Bidirectional search or state hashing with more efficient structures.

---

## Troubleshooting

- If the program reports the puzzle as unsolvable, re-check the tile permutation and blank position; the solver properly uses the inversion+blank rules.
- If you see no solution for a puzzle that should be solvable, ensure you entered tiles in the correct order and the blank index is correct (0-based).
- If runtime/memory usage is excessive for larger puzzles (e.g., 24-puzzle), consider switching to IDA* or using a specialized solver.

---

## Contributing

Contributions are welcome. Suggested improvements:
- Add automated tests for solvability function and A* behavior.
- Add a non-interactive mode (CLI flags) so the solver can accept input via command-line arguments or files for batch testing.
- Implement alternative heuristics (linear conflict, pattern databases) and compare performance.
- Provide an option to output intermediate boards or to visualize moves.

To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-fix`
3. Make changes, run tests (if available), and commit.
4. Open a pull request describing your changes.

---

## License

Add a license file to the repository if you wish to make the code open source. Example: MIT License. If you want, I can add a LICENSE file for you.

---

If you'd like, I can:
- Rename `n_puzzle_solver.py` and open a PR with the README update and any other small edits, or
- Create a non-interactive CLI wrapper (arguments + file input) so you can run puzzles from scripts or CI.