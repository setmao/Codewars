def is_valid_walk(walk: List[str]) -> bool:
    if len(walk) != 10:
        return False

    if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
        return True
    else:
        return False

