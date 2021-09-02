def duplicate_encode(word):
    return "".join(["(" if word.upper().count(w.upper()) == 1 else ")" for w in word])
