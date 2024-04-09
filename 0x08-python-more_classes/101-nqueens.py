#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen at position (row, col) on the board is safe.

    Args:
    - board: The current state of the chessboard.
    - row: The row index of the position to check.
    - col: The column index of the position to check.
    - N: The size of the chessboard.

    Returns:
    - True if it's safe to place a queen at position (row, col), False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N, solutions):
    """
    A utility function to recursively find all solutions to the N queens problem.

    Args:
    - board: The current state of the chessboard.
    - row: The current row to consider placing a queen.
    - N: The size of the chessboard.
    - solutions: A list to store all found solutions.
    """
    if row == N:
        solutions.append([[i, col] for i, col in enumerate(board)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_nqueens(N):
    """
    Solve the N queens problem and print all possible solutions.

    Args:
    - N: The size of the chessboard.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_nqueens(N)
