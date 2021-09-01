def solution(string,markers):
    
    # First, split all the lines to a list.
    list = string.split("\n")
    
    
    # Second, for loop of each item in the list
    for index, item in enumerate(list):
        
        # Create a new_item for each item and initilize it with the current item
        new_item = item
        
        # Now for each marker we have
        for marker in markers:
            
            # Check if it is appear in the current item
            if marker in list[index]:
                
                # If so - take it index
                i = item.index(marker)
                
                # And make the new_item to be the current item until that index, and strip it
                new_item = item[:i].strip()
                
                # Now put the new_item instead of the current item
                list[index] = new_item
    
    # Join the list with \n so it will return to itself, and return it
    return "\n".join(list)
