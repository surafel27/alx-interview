#!/usr/bin/python3
'''The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard'''
import sys


def is_safe(board, row, col, N):
    '''check for the boadr'''
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    '''solve the number of queens'''
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    solutions = []

    def print_solution(board):
        '''print the solution'''
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)

    def place_queens(row):
        '''place the quee in row'''
        if row == N:
            print_solution(board)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                place_queens(row + 1)
                board[row] = -1

    place_queens(0)

    for solution in solutions:
        print(solution)


def main():
    '''main finction'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    '''python starts exection here'''
    main()
