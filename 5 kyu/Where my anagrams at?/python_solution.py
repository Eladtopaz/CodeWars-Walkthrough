def anagrams(word, words):
    
    # Make a new dict with the count of every char in the original word
    word_dict = {}
    for char in word:
        word_dict[char] = word.count(char)
        
    # Make a list to hold the results
    list = []
    
    # For every word in the list
    for w in words:
        
        # Make a new dict with the count of ever char in the word
        new_dict = {}
        for c in w:
            new_dict[c] = w.count(c)
        
        # If the dicts are same
        if new_dict == word_dict:
            
            # Add to list
            list.append(w)
        
    # Return the result
    return list
    
