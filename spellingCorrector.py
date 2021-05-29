import nltk
import json
from fidel import Fidel
class SpellingCorrector:
    def __init__(self):
        pass

    def sortByValue(self, dictForSort):
        return sorted(dictForSort.items(), key = lambda x:x[1])

    def suggestions(self, word, word_suggestions):
        suggested = {}
        for word_suggestion in word_suggestions:
            measure = {}
            #word frequency
            measure['freq'] = word_suggestion[1]

            #Step-3: Measure the similarity of the words
            measure['distance'] = nltk.edit_distance(word_suggestion[0], word) #similarity is measure using edit distance
            
            suggested[word_suggestion[0]] = measure
            #Step-4: Choose the most five close words, apply distribution when words have the same distance
        return suggested
    '''
    def normalizingPhenome(geez):
        normalized = {}
        phenomes = Fidel.phenome()
        new_word = ''
        for letter in geez:
            if letter in phenomes:
                new_word += phenomes[letter]
            else:
                new_word += letter
        normalized.append(new_word)

    '''

    def spellingCorrector(self, word, geez, geez_dict):
        #Step-1: Match the input-geez with the geez dictionary
        suggestions_dict = {}
        '''
        #If the input is in the geez dictionary then look the input in the geez dictionary.
        if geez in geez_dict:
            #Step-2: Retriev all the words with the same geez form.
            word_suggestions = geez_dict[geez]
            
            #Step-4: Choose the most five close words, apply distribution when words have the same distance
            suggestions_dict[word] = SpellingCorrector().suggestions(word, word_suggestions)
        else:
            #Step-1: Measure similarity of the geez form of the input with geez words from the dictionary
            #Step-2: Choose the most five close words, apply distribution when words have the same distance
        '''
        
        suggestions_dict_geez = {}
        word_suggestions = []
        for geez_d in geez_dict:
            
            #similarity measure of misspelt in geez form and geez words from dictionary
            suggestions_dict_geez[geez_d] = nltk.edit_distance(geez, geez_d)

        top_5_suggestions = SpellingCorrector().sortByValue(suggestions_dict_geez)[0:10]

        #print(top_5_suggestions)
        #top_10_suggestions = SpellingCorrector().sortByValue(suggestions_dict_geez)
            
        #sort geez suggestion based on their distance
        '''
        for suggested_geez in suggestions_dict_geez:
            word_suggestions += geez_dict[suggested_geez]
        '''
        for picks in top_5_suggestions:
            word_suggestions += geez_dict[picks[0]]
            
        suggestions_dict[word] = SpellingCorrector().suggestions(word, word_suggestions) #put it under else part
        return suggestions_dict
    







