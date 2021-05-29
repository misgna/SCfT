count = 0
total = 0
words = {}

#suggestions = open('Data/top5.json', 'r')
suggestions = open('Data/top10.json', 'r')
misspelt = open('Data/misspelt.txt', 'r')


for ms in misspelt:
    words = ms.replace('\n', '').split(' : ')
    start = "{'" + words[0] + "':"
    total += 1
    for suggestion in suggestions:

        if suggestion.replace('\n', '').startswith(start):
        
            suggestion1 = "{'" +  words[1] + "':"
            suggestion2 = " '" + words[1] + "':"
            
            if  (suggestion1 in suggestion) or (suggestion2 in suggestion):
                count += 1
        break
    

accuracy = count * 100 / total

print("total number of misspelt words", total)
print("Corrected words", count)
print("Accuracy", accuracy)


    