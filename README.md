# N-Puzzle Solver (A* Algorithm with Manhattan Distance)

This project contains a Python implementation of the N-Puzzle solver using the A* search algorithm with the Manhattan distance heuristic to find the optimal path from any solvable initial state to the standard goal state.

The solver supports N-Puzzles where N+1 is a perfect square (e.g., 3x3 (N=8), 4x4 (N=15), 5x5 (N=24)).

---

## How to Run the Solution

### 1. Prerequisites

You must have **Python 3** installed on your system.

### 2. Execution

1.  Save the provided code as a file named `n_puzzle_solver.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `n_puzzle_solver.py`.
4.  Run the script using the following command:

    ```bash
    python n_puzzle_solver.py
    ```

### 3. User Input Prompts

The program will guide you through three input steps:

| Prompt | Example | Description |
| :--- | :--- | :--- |
| `Enter the number of blocks (N)` | `15` | The size of the puzzle (e.g., 8 for 3x3, 15 for 4x4). |
| `Enter the STARTING index for the empty block (0)` | `4` | The index (0 to N) where the empty block (0) starts. |
| `Remaining Tiles (separated by spaces)` | `1 2 3 4 5 7 8 6` | The arrangement of the numbered tiles (1 to N). **Do NOT include 0.** |

---

## Design Notes and Algorithm Details

### 1. Algorithm Choice: A* Search

* The A* algorithm is used because it guarantees finding the **optimal path** (shortest sequence of moves) by balancing the cost of the path taken so far ($G$-score) and the estimated cost to reach the goal ($H$-score).
* **A\* Formula:** $F(n) = G(n) + H(n)$

### 2. Heuristic: Manhattan Distance

* **Manhattan Distance ($H$-score):** This heuristic calculates the sum of the horizontal and vertical distances of every tile from its correct position in the goal state.
* **Admissibility:** Manhattan distance is an **admissible** heuristic, meaning it never overestimates the true cost to reach the goal. This property is essential for A\* to guarantee optimality.

### 3. State Representation

* The board state is stored as a **tuple of tuples** (`tuple(tuple(row) for row in board)`). This is crucial because tuples are **immutable** and can therefore be used as dictionary keys in the `g_scores` hash map for efficient lookup.

### 4. Solvability Check

* The `is_solvable()` method uses the **parity rule** to quickly determine if the given starting state can lead to the goal state. This prevents the A\* algorithm from wasting time searching an unsolvable space.
    * **Odd Grid Side (e.g., 3x3):** Solvable if the number of inversions is **even**.
    * **Even Grid Side (e.g., 4x4):** Solvable if the parity of (inversions + row of the blank from the bottom) is **odd**.

### 5. Goal State

* The goal state is **fixed** to the standard configuration where tiles $1$ through $N$ are in ascending order, and the empty block ($0$) is in the **bottom-right corner**. The input parameter $I$ is hardcoded to $-1$ in the input gathering step to signal this standard goal.
