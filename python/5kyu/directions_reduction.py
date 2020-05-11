def dirReduc(arr):

    transform_direction_dict = {
        "NORTH": 1,
        "SOUTH": -1,
        "EAST": 0.5,
        "WEST": -0.5
    }

    stack = []

    for direction in arr:
        if stack == []:
            stack.append(transform_direction_dict[direction.upper()])
            continue

        if stack[-1] + transform_direction_dict[direction.upper()] == 0:
            stack.pop(-1)
        else:
            stack.append(transform_direction_dict[direction.upper()])

    return [{v: k for k, v in transform_direction_dict.items()}[x] for x in stack]

