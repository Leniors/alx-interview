#!/usr/bin/python3
""" Solves N queens puzzle """
import sys


def print_sol(board):
    """ Prints the board as a list of lists of indices """
    solution = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def is_valid(board, row, column):
    """ Checks if the place of `row` and `column` is valid """
    n = len(board)

    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_queens_util(board, column):
    """ Utilizes backtracking to solve the N Queens problem """
    n = len(board)
    if column >= n:
        print_sol(board)
        return True

    res = False
    for i in range(n):
        if is_valid(board, i, column):
            board[i][column] = 1
            res = n_queens_util(board, column + 1) or res
            board[i][column] = 0

    return res


def n_queens(n):
    """ Places N non-attacking queens on an NxN chessboard """
    board = [[0 for _ in range(n)] for _ in range(n)]
    n_queens_util(board, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    n_queens(int(sys.argv[1]))