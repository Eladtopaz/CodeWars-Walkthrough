def digital_root(n):
    
    new_number = n
    while True:
        
        new_number = sum([int(x) for x in str(new_number)])
        if new_number <= 9:
            return new_number    
