#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Usage:
     ./101-nqueens.py N

Where N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, N, solutions):

    if row == N:
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        solutions.append(solution)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_nqueens_util(board, row + 1, N, solutions) or res
            board[row][col] = 0

    return res


def solve_nqueens(N):

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    if not solutions:
        print("No solution exists")
        sys.exit(1)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
