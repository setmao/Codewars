def rgb(r: int, g: int, b: int) -> str:
    result = ''
    for i in [r, g, b]:
        if i > 255:
            result += 'FF'
        elif i < 0:
            result += '00'
        else:
            result += "{:02X}".format(i)

    return result

