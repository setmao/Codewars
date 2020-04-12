def goodVsEvil(good: str, evil: str) -> str:
    good_default = [1, 2, 3, 3, 4, 10]
    evil_default = [1, 2, 2, 2, 3, 5, 10]

    good_score = sum([x * int(y) for x, y in zip(good_default, good.split())])
    evil_score = sum([x * int(y) for x, y in zip(evil_default, evil.split())])

    if good_score > evil_score:
        return 'Battle Result: Good triumphs over Evil'
    elif good_score < evil_score:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'

