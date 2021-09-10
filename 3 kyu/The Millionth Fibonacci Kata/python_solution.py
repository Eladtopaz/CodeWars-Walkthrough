def fib(n):
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    elif n > 0:
        
        def fib_pos(n):
    
            a, b = 0, 1
            for i in range(n):
                    a, b = b, a + b

            return a
    
        return fib_pos(n)

    else:
        
        def fib_neg(n):
    
            a, b = 0, 1
            for i in range(-n):
                a, b = b, a - b
            return a
        
        return fib_neg(n)
