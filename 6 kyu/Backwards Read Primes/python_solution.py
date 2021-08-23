from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

def backwards_prime(start, stop):
    prime_list = []
    
    for num in range(start, stop+1):
        if is_prime(num) and is_prime(int(str(num)[::-1])) and num != int(str(num)[::-1]):
            prime_list.append(num)
                
    
    return prime_list
