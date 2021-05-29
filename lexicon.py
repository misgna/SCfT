import json

class GeezWords:
    def __init__(self):
        pass

    def amharicWords(self):
        filepath = "Data/allwords.txt"
        amharic_words = []

        with open(filepath, encoding = "utf8") as file:
            for line in file:
                amharic_words.append(line.rstrip())
        return amharic_words

    def geezWords(self):
        filepath = "Data/output.json"
        geez_words = {}

        with open(filepath, encoding="utf8") as file:
            data = json.load(file)
            for record in data['kalat']:
                geez_words[record['geez']] = record['words']
        return geez_words

    def misspeltWords(self):
        filepath = "Data/misspelt.txt"
        misspelt_words = {}

        with open(filepath, encoding = "utf8") as file:
            for line in file:
                words = line.split(" : ")
                misspelt_words[words[0]] = words[1].rstrip()
        return misspelt_words



        