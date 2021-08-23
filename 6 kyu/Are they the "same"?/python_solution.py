def comp(array1, array2):
    
    if None in (array1, array2) or len(array1) != len(array2):
        return False
    new_arr = [a ** 2 for a in array1]
    for a in new_arr:
        if new_arr.count(a) != array2.count(a):
            return False
            
    return True
