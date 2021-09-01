# Basically cheating but I don't care :)
import itertools

def permutations(string):
    per_list = []
    for permutation in itertools.permutations(string):
        per_list.append("".join(permutation))
        
    return set(per_list)
