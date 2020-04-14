def valid_parentheses(string: str) -> bool:
    stack = []
    for i in string:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

