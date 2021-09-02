def decode_bits(bits):

    bits = bits.strip("0")
    dot_size = dash_size = size = 0
    for b in bits:
        if b == "1":
            size += 1
        if b == "0":
            break
    
    
    if size % 3 == 0:
        size_2 = (size // 3)
        if size_2 * 7 * "0" in bits or size_2 * 1 * "0" in bits or size_2 * 3 * "0" in bits:
            dot_size = size // 3
            dash_size = size
        else:
            dot_size = size
            dash_size = size * 3 
        
        if ("0" + (size_2 * "1") + "0") not in bits:
            if size * 7 * "0" in bits or size * 1 * "0" in bits or size * 3 * "0" in bits:
                dot_size = size
                dash_size = size * 3
    else:
        dot_size = size
        dash_size = size * 3
    
    count = 0
    current = "1"
    morse_string = ""
    for b in bits:
        if b == current:
            count += 1
        else:
            if current == "1" and count == dot_size:
                morse_string += "."
            elif current == "1" and count == dash_size:
                morse_string += "-"
            elif current == "0" and count == dot_size:
                pass
            elif current == "0" and count == dot_size * 3:
                morse_string += " "
            elif current == "0" and count == dot_size * 7:
                morse_string += " " * 3
                
            current = b
            count = 1
            
    if current == "1" and count == dot_size:
        morse_string += "."
    elif current == "1" and count == dash_size:
        morse_string += "-"
    elif current == "0" and count == size:
        pass
    elif current == "0" and count == size * 3:
        morse_string += " "
    elif current == "0" and count == size * 7:
        morse_string += " " * 3
    
    return morse_string

    
def decode_morse(morseCode):
    """ So, to mange doing this in 1 line:
        I took the string I got and removed the leading or trailing spaces using strip()
        Then, I used split(" ") to split it to a list, by the spaces in the string.
        Then, If the item is in the MORSE_CODE table, get it value, if not, put " ".
        Now, use "".join() to make that list to a string, and the problem - each space between words become 3 times.
        So, I splited it once again using split() and joined it with spaces using " ".join(), return the string and it worked,
        One line.
    """
    return " ".join("".join([MORSE_CODE[m] if m in MORSE_CODE else " " for m in morseCode.strip().split(" ")]).split())
