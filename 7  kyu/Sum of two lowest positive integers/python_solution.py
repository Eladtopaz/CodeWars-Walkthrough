import sys

def sum_two_smallest_numbers(numbers):
    """ The function take a list and sum the 2 smallest integers in the list.
    The list should have only positive values.
    """
    
    # First we will save the 2 highest values an integer can hold.
    first_min = sys.maxsize * 2 + 1
    second_min = sys.maxsize * 2 + 1
    
    # Second we will loop on the whole list and try to find the small integers
    for num in numbers:
        
        # If the current number is smaller then first_min
        if num < first_min:
            
            # We will keep the first_min ad second_min and the current num as first_min
            second_min = first_min
            first_min = num
            
        # If not and if the current number is smaller then the second_min
        elif num < second_min:
            
            # We will keep the current min as the second_min
            second_min = num
            
    return first_min + second_min
