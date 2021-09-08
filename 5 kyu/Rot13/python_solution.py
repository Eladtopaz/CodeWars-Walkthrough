def rot13(message):
    letters = "abcdefghijklmnopqrstuvwxyz"
    bigger_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_13 = "nopqrstuvwxyzabcdefghijklm"
    letters_bigger_13 = "NOPQRSTUVWXYZABCDEFGHIJKLM"
    
    new_message = ""
    for char in message:
        if char in letters:
            new_message += letters_13[letters.index(char)]
        elif char in bigger_letters:
            new_message += letters_bigger_13[bigger_letters.index(char)]
        else:
            new_message += char
    
    return new_message
