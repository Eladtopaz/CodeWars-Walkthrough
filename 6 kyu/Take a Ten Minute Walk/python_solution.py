def is_valid_walk(walk):
    #determine if walk is valid
    number_of_s = number_of_w = number_of_n = number_of_e = 0
    
    # First we make sure the walk will be 10 minutes
    if(len(walk) != 10):
        return False
    
    # Then we will count each direction
    for direction in walk:
        if direction == "s":
           number_of_s += 1
        if direction == "e":
            number_of_e += 1
        if direction == "n":
            number_of_n += 1
        if direction == "w":
            number_of_w += 1
    
    # We will check if n == s and e == w, which will lead us to the starting point
    if (number_of_n == number_of_s) and (number_of_w == number_of_e):
        return True
    
    # Else - return False
    return False
