import re

def increment_string(string):
    
    if string == "":
        return "1"
    
    elif string[-1].isdigit():
        pattern = re.compile(r'^(.*?)(\d+)$')
        matches = pattern.finditer(string)
        match = next(matches)
        
        match_number = match.group(2)
        number = str(int(match_number) + 1)
        number = number.zfill(len(match_number))
        return match.group(1) + number
            
    else:
        return string + "1"
