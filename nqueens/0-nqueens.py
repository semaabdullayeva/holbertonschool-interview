#!/usr/bin/python3
import sys

# Function to check if the position is safe for the queen
def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

# Recursive function to solve N Queens problem
def solve_nqueens(board, row, N, solutions):
    if row == N:
        # All queens are placed correctly
        solution = []
        for i in range(N):
            solution.append([i, board[i]])
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)

# Main function to handle input and solve the problem
def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
