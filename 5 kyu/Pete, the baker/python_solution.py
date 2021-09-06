def cakes(recipe, available):
    
    # First create a list with the length of the recipe, each slot with 0
    cakes_number = [0] * len(recipe)
    
    # Then i to run on the list
    i = 0
    
    # For every key and value in the recipe
    for key, value in recipe.items():
        
        # Try to see how much of it available
        try:
            
            # Put the result in the correct index in the list
            cakes_number[i] = available[key] // value
            
        # If the key isn't exist
        except KeyError:
            
            # Means we can't bake 1 cake, don't have ingerdient
            cakes_number[i] = 0
            break
        
        # For the next ingerdient, move to the next index in the list
        i += 1
        
    # Return the mininum from the list.
    return min(cakes_number)
