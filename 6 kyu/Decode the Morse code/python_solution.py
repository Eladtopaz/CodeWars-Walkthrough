def decodeMorse(morse_code):
    """ So, to mange doing this in 1 line:
        I took the string I got and removed the leading or trailing spaces using strip()
        Then, I used split(" ") to split it to a list, by the spaces in the string.
        Then, If the item is in the MORSE_CODE table, get it value, if not, put " ".
        Now, use "".join() to make that list to a string, and the problem - each space between words become 3 times.
        So, I splited it once again using split() and joined it with spaces using " ".join(), return the string and it worked,
        One line.
    """
    return " ".join("".join([MORSE_CODE[m] if m in MORSE_CODE else " " for m in morse_code.strip().split(" ")]).split())
