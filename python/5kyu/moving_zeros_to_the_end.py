def move_zeros(array: list) -> list:
    return_list = []
    zero_count = 0

    for element in array:
        if element != 0 or str(element) == "False":
            return_list.append(element)
        else:
            zero_count += 1

    return_list.extend([0 for i in range(zero_count)])

    return return_list

