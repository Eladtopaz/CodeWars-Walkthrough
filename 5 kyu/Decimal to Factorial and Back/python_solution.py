import math

converter = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
    "16": "G",
    "17": "H",
    "18": "I",
    "19": "J",
    "20": "K",
    "21": "L",
    "22": "M",
    "23": "N",
    "24": "O",
    "25": "P",
    "26": "Q",
    "27": "R",
    "28": "S",
    "29": "T",
    "30": "U",
    "31": "V",
    "32": "W",
    "33": "X",
    "34": "Y",
    "35": "Z"
}
def dec_2_fact_string(nb):
    
    st = "0"
    x = 2
    while nb > 0:
        new_digit = str(nb % x)
        if new_digit in converter:
            new_digit = converter[new_digit]
        st += new_digit
        nb = nb // x
        x += 1
    return st[::-1]

def fact_string_2_dec(string):
    
    key_list = list(converter.keys())
    val_list = list(converter.values())
    print(f"{string=}")
    result = 0
    x = 0
    for s in string[::-1]:
        if s in val_list:
            position = val_list.index(s)
            result += int(key_list[position]) * math.factorial(x)
        else:
            result += math.factorial(x) * int(s)
        x += 1
    return result
