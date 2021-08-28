def ensure_question(s):
    return s + "?" if len(s) == 0 or s[-1] != "?" else s
