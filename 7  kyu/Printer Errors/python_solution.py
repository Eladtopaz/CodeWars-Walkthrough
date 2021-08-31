def printer_error(s):
    
    # Create a string that contain all the ligit letters
    ok_letters = "abcdefghijklm"
    
    # Make sum for the errors, with 0 at first.
    error_num = 0
    
    # Check every char on the string 
    for char in s:
        
        # If he is not ok
        if char not in ok_letters:
            
            # Put another error
            error_num += 1
    
    return (f"{error_num}/{len(s)}")
