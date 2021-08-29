def longest_repetition(chars):
    c = ""
    l = 0
    for i, char in enumerate(chars):
        temp_c = char
        temp_l = 0
        for new_c in chars[i:]:
            if new_c == temp_c:
                temp_l += 1
            else:
                break
        if temp_l > l:
            l = temp_l
            c = temp_c
    
    return (c, l)
