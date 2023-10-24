class RomanNumerals:    
    
    
    @staticmethod
    def to_roman(val : int) -> str:
        number_dict = {1:"I",
                       5: "V",
                       10: "X",
                       50: "L",
                       100: "C",
                       500: "D",
                       1000: "M"}
        
        if val in number_dict.keys():
            return number_dict[val]
    
        roman = ""
        
        while val > 0:
            
            if val >= 1000:
                roman = roman + "M"
                val -= 1000
            elif val >= 900:
                roman = roman + "CM"
                val -= 900
            elif val >= 500:
                roman = roman + "D"
                val -= 500
            elif val >= 400:
                roman = roman + "CD"
                val -= 400
            elif val >= 100:
                roman = roman + "C"
                val -= 100
            elif val >= 90:
                roman = roman + "XC"
                val -= 90
            elif val >= 50:
                roman = roman + "L"
                val -= 50
            elif val >= 40:
                roman = roman + "XL"
                val -= 40 
            elif val >= 10:
                roman = roman + "X"
                val -= 10
            elif val >= 9:
                roman = roman + "IX"
                val -= 9 
            elif val >= 5:
                roman = roman + "V"
                val -= 5
            elif val >= 4:
                roman = roman + "IV"
                val -= 4 
            elif val >= 1:
                roman = roman + "I"
                val -= 1                 
        
        return roman

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_dict = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000}
        
        if len(roman_num) == 1:
            return roman_dict[roman_num[0]]
        
        i = 0
        sum = 0

        while (i < len(roman_num) - 1):
            if roman_dict[roman_num[i]] < roman_dict[roman_num[i + 1]]:
                sum += roman_dict[roman_num[i + 1]] - roman_dict[roman_num[i]]
                i += 2
            else:
                sum += roman_dict[roman_num[i]]
                i += 1
            
            if (i == len(roman_num) - 1):
                sum += roman_dict[roman_num[i]]
        return sum
