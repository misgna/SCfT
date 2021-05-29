'''
GeezSpell is a spelling corrector for languages that use geez letters.
It suggests words for a misspelt word without transliterating.
'''

from lexicon import GeezWords
from wordToGeez import WordToGeez
from transliterate import Transliteration

from spellingCorrector import SpellingCorrector

#Step-1: Load geez dictionary, amharic words and misspelt words(for testing)
geez_words = GeezWords().geezWords() #load the geez dictionary
amharic_words = GeezWords().amharicWords() #list of amharic words
misspelt_words = GeezWords().misspeltWords() #misspet words with their corrections
#dictionary of suggested corrections
suggestions = {}

#test ground for transliteration
'''
f = open('tr_misspelt.txt', 'w')
transliterated = ''
for word in misspelt_words:
    print(word)
    transliterated += Transliteration().geez_to_latin(word) + '\n'
   
f.write(transliterated)
f.close()
print("misspelt words are transliterated")
    
'''


#Step-2: Check if the word is misspelt; word is not in the lexicon
for misspelt_word in misspelt_words: 
    if misspelt_word not in amharic_words:

        #Step-3: Transform word into geez; First form of geez structure
        geez_word, word = WordToGeez().word_to_geez(misspelt_word)
        #print(misspelt_word, geez_word)
            
        suggestions = SpellingCorrector().spellingCorrector(word, geez_word, geez_words)
        print(suggestions)