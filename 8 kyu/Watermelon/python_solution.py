def divide(weight):
    if weight % 2 != 0:
        return False
    
    for i in range(1, weight):
        if i % 2 == 0 and (weight - i) % 2 == 0:
            return True
        
    return False
