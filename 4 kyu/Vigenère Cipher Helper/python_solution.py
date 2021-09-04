class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self._key = key
        self._alphabet = alphabet
        self._alphabet_arr = [alphabet[i: len(alphabet)] + alphabet[:i] for i in range(0, len(alphabet))]
    
    def encode(self, text):
        
        old_key = self._key
        if len(text) != len(self._key):
            r = len(text) - len(self._key)
            for i in range(r):
                self._key += self._key[i]
                
        new_text = ""
        for i in range(0, len(text)):
            if text[i] not in self._alphabet:
                new_text += text[i]
            else:
                row = self._alphabet.index(self._key[i])
                column = self._alphabet.index(text[i])
                new_text += self._alphabet_arr[row][column]
        self._key = old_key
        return new_text
                
    
    def decode(self, text):
        
        old_key = self._key
        if len(text) != len(self._key):
            r = len(text) - len(self._key)
            for i in range(r):
                self._key += self._key[i]
        
        new_text = ""
        for i in range(0, len(text)):
            if text[i] not in self._alphabet:
                new_text += text[i]
            else:
                row = self._alphabet.index(self._key[i])
                row = self._alphabet_arr[row]
                column = row.index(text[i])
                new_text += self._alphabet[column]
        
        self._key = old_key
        return new_text
