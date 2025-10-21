import heapq
import math


class N_Puzzle_Solver:
    def __init__(self, N, I, initial_layout):
        self.N_blocks = N
        self.Side = int(math.sqrt(N + 1))
        if self.Side * self.Side != N + 1:
            raise ValueError("Invalid N. N+1 must be a perfect square (e.g., N=8, 15, 24).")
        
        self.I = I
        self.start_board = self._flat_to_square(initial_layout)
        self.goal_board = self._get_goal_board()
        self.goal_coords = self._get_goal_coordinates()

    def _flat_to_square(self, flat_list):
        if len(flat_list) != self.Side * self.Side:
            raise ValueError(f"Initial layout size ({len(flat_list)}) does not match board size ({self.Side*self.Side}).")
        
        board = []
        for i in range(0, len(flat_list), self.Side):
            board.append(flat_list[i:i + self.Side])
        return tuple(tuple(row) for row in board)

    def _get_goal_board(self):
        tiles = list(range(1, self.N_blocks + 1)) + [0]
        goal = self._flat_to_square(tiles)
        return goal

    def _get_goal_coordinates(self):
        coords = {}
        for r in range(self.Side):
            for c in range(self.Side):
                tile_num = self.goal_board[r][c]
                coords[tile_num] = (r, c)
        return coords

    def _manhattan_distance(self, board):
        distance = 0
        for r in range(self.Side):
            for c in range(self.Side):
                tile = board[r][c]
                if tile == 0:
                    continue
                
                goal_r, goal_c = self.goal_coords[tile]
                distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def is_solvable(self):
        flat_list = [tile for row in self.start_board for tile in row if tile != 0]
        inversions = 0
        
        for i in range(len(flat_list)):
            for j in range(i + 1, len(flat_list)):
                if flat_list[i] > flat_list[j]:
                    inversions += 1
        
        blank_r, blank_c = next(((r, c) for r in range(self.Side) for c in range(self.Side) if self.start_board[r][c] == 0))
        blank_row_from_bottom = self.Side - blank_r

        if self.Side % 2 != 0:
            return inversions % 2 == 0
        else:
            return (inversions % 2) != (blank_row_from_bottom % 2)

    def solve(self):
        if not self.is_solvable():
            return -1, 

        start_h = self._manhattan_distance(self.start_board)
        open_set = [(start_h, 0, self.start_board, [])] 
        g_scores = {self.start_board: 0}
        
        moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

        while open_set:
            f, g, current_board, path = heapq.heappop(open_set)

            if current_board == self.goal_board:
                return g, path

            blank_r, blank_c = next(((r, c) for r in range(self.Side) for c in range(self.Side) if current_board[r][c] == 0))
            
            for dr, dc, move_char in moves:
                new_r, new_c = blank_r + dr, blank_c + dc

                if 0 <= new_r < self.Side and 0 <= new_c < self.Side:
                    temp_board = [list(row) for row in current_board]
                    
                    temp_board[blank_r][blank_c], temp_board[new_r][new_c] = temp_board[new_r][new_c], temp_board[blank_r][blank_c]
                    
                    next_board = tuple(tuple(row) for row in temp_board)
                    new_g = g + 1

                    if next_board not in g_scores or new_g < g_scores[next_board]:
                        g_scores[next_board] = new_g
                        h = self._manhattan_distance(next_board)
                        f = new_g + h
                        new_path = path + [move_char]
                        
                        heapq.heappush(open_set, (f, new_g, next_board, new_path))
        
        return -1, 


def get_user_input():
    
    
    while True:
        try:
            N = int(input("Enter the number of blocks (N) [e.g., 8, 15]: "))
            side = int(math.sqrt(N + 1))
            if side * side != N + 1 or N < 3:
                print("Error: N+1 must be a perfect square (e.g., 8, 15, 24) and N must be >= 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer for N.")

    total_cells = N + 1
    
    I = -1 
    
    print(f"\nDefining Start State ---> ")
    while True:
        try:
            start_index_0 = int(input(f"Enter the STARTING index for the empty block (0) (0 to {N}): "))
            if 0 <= start_index_0 <= N:
                break
            else:
                print(f"Error: Index must be between 0 and {N}.")
        except ValueError:
            print("Invalid input. Please enter an integer for the index.")

    print(f"\nEnter the {N} remaining tiles (1 to {N}), separated by spaces.")
    print(f"Example for {side}x{side} (excluding 0): {list(range(1, N+1))}")
    
    while True:
        try:
            layout_str = input("Remaining Tiles (separated by spaces): ")
            tiles_N = [int(x) for x in layout_str.split()]
            
            if len(tiles_N) != N:
                print(f"Error: You must enter exactly {N} tiles (1 to {N}).")
                continue
                
            required_tiles = set(range(1, N + 1))
            if set(tiles_N) != required_tiles:
                 print(f"Error: Tiles must be a permutation of {required_tiles}. Check for duplicates or missing numbers (0 should NOT be included).")
                 continue

            break
        except ValueError:
            print("Invalid input. Ensure all tiles are numbers separated by spaces.")
            
    final_initial_layout = tiles_N[:] 
    final_initial_layout.insert(start_index_0, 0) 

    print(f"\nSystem Assembled Initial Layout: {final_initial_layout}")
    
    return N, I, final_initial_layout
if __name__ == "__main__":
    try:
        N_input, I_input, layout_input = get_user_input()
        
        solver = N_Puzzle_Solver(N=N_input, I=I_input, initial_layout=layout_input)

        print(f"\n{solver.Side}x{solver.Side} N-Puzzle Solver--->")
        print(f"Initial State:\n{solver.start_board[0]}")
        for row in solver.start_board[1:]:
            print(row)
        
        is_solvable = solver.is_solvable()
        print(f"\nSolvability Check: {'it is SOLVABLE-> because the rule is fulfilled' if is_solvable else 'UNSOLVABLE'}")

        if is_solvable:
            print("\n Running A* Search for Optimal Path... ")
            path_length, moves_list = solver.solve()
            
            if path_length != -1:
                print("\n Solution Found ---> ")
                print(f"Optimal Path Length (G-score): {path_length}")
                print("Sequence of Moves that you need to follow:")
                for move in moves_list:
                    print(move)
            else:
                 print("\n Error ")
                 print("The search finished without finding the goal (should not happen for a solvable puzzle).")
        else:
            print("\n Result ")
            print("Since the puzzle is unsolvable, no search will be performed.")
            
    except ValueError as e:
        print(f"\n Fatal Error: {e}")