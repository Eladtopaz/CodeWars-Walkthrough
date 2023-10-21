def array_diff(a, b):
    new_a = []
    
    for chr in a:
        if chr not in b:
            new_a.append(chr)
    return new_a
