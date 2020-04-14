def spin_words(sentence: str) -> str:
    words = sentence.split(' ')
    new_sentence = []
    for word in words:
        if len(word) >= 5:
            new_sentence.append(word[::-1])
        else:
            new_sentence.append(word)

    return ' '.join(new_sentence)

