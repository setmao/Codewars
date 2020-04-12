def find_next_square(sq: int) -> int:
    from math import sqrt

    if int(sqrt(sq)) == sqrt(sq):
        return int(sqrt(sq) + 1) ** 2
    else:
        return -1

