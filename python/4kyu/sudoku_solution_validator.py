from typing import List


def valid_solution(board: List[list]) -> bool:
    valid_list = sorted([i for i in range(1, 10)])

    for row in board:
        if sorted(row) != valid_list:
            return False

    for col in range(len(board)):
        if sorted([row[col] for row in board]) != valid_list:
            return False

    for block in range(9):
        x = (block % 3) * 3
        y = (block // 3) * 3
        if sorted([board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]) != valid_list:
            return False

    return True

