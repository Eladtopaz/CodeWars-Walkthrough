def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]
