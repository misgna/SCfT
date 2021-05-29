from fidel import Fidel

class WordToGeez:
    def __init__(self):
        pass
    
    def word_to_geez(self, token):
        
        fidels = Fidel().fidel_to_geez()

        gzWord = "" #a word where all letters are transformed to geez form
        word = "" #original word form
        for char in token:
            if (char in fidels) and (char is not ''):
                gzWord += fidels[char]
                word += char
        return gzWord, word

    def words_to_geez(self, tokens):
        geezWords = {}
        tokens = tokens.keys()
        l2g = WordToGeez()

        for token in tokens:
            gzWord, word = l2g.word_to_geez(token)
            if (gzWord in geezWords):
                words = geezWords[gzWord]
                if word not in words:
                    geezWords[gzWord].append(word)
            elif word is not '':
                words = [word]
                geezWords[gzWord] = words
            else:
                pass
        return geezWords