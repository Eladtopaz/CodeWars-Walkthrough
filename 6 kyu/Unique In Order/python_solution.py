def unique_in_order(iterable):
    
    # Create an empty list
    list = []
    
    # Loop the iterable object
    for i in iterable:
        
        # If the list is empty,
        if len(list) == 0:
            
            # Add the last item
            list.append(i)
            
        # If the last item isn't in the last position of the list
        if i != list[-1]:
            
            # Add him
            list.append(i)
    
    return list
