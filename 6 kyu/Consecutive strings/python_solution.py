def longest_consec(strarr, k):
    
    # If one of this condition met - return ""
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    
    
    # Create i to run on the strarr and empty list for the new strings
    i, new_list = 0, []
    
    
    # Stop when the length on strarr is smaller then i + k 
    # Because each loop we will take k positions ahead
    while(i <= len(strarr) - k):
        
        # Create the m for the inter loop
        m = i + 1
        
        # Start the new string with the current string, in i position
        new_string = strarr[i]
        
        # Run on the next k - i positions ahead
        while(m - i < k):
            
            # Add them to the string
            new_string += strarr[m]
            m += 1
        
        # And append to the new list.
        new_list.append(new_string)
        i += 1
    
    # Sort the list so the first longest string will be first and return it
    new_list.sort(key = len, reverse = True)
    return new_list[0]
