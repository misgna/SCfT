from fidel import Fidel
class Transliteration:
    def __init__(self):
        pass
    
    def geez_to_latin(self, token):
        
        letters = Fidel().fidel_to_english()

        transliterated = "" #a word where all letters are transformed to latin form

        for char in token:
            if char in letters:
                transliterated += letters[char]
            else:
                transliterated += char

        return transliterated