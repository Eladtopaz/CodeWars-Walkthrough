def sort_array(source_array):

    # Make a second list with all the odd numbers
    second_arr = [item for item in source_array if item % 2 == 1]
    
    # Sort the list
    second_arr.sort()
    
    # Make iterator from that list
    iter_obj = iter(second_arr)
    
    # Now return a new list, if the number is odd, take a number from the iterator, if the number is
    # even, keep him.
    return [next(iter_obj) if item % 2 == 1 else item for item in source_array]
