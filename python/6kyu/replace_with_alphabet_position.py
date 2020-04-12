def alphabet_position(text: str) -> str:
    return_str = ''

    for char in text.lower():
        if 97 <= ord(char) <= 122:
            if return_str:
                return_str = '{} {}'.format(return_str, str(ord(char) - 96))
            else:
                return_str += str(ord(char) - 96)

    return return_str

