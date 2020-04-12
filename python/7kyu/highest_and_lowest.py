def high_and_low(numbers: int) -> str:
    return "{} {}".format(max([int(i) for i in numbers.split()]), min([int(i) for i in numbers.split()]))

