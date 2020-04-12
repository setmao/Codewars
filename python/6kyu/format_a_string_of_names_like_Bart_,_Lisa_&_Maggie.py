def namelist(names: List[dict]) -> str:
    if not names:
        return ''

    return_str = names[0]['name']

    for index in range(len(names) - 1):
        if index == len(names) - 2:
            return_str += ' & '
        else:
            return_str += ', '

        return_str += names[index + 1]['name']

    return return_str

