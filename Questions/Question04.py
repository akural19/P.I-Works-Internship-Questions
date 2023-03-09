import numpy as np

try: 
    file = open("country_vaccination_stats.csv", "r")
    newFile = open("imputed_country_vaccination_stats.csv", "w")
    lines = file.readlines()
    
    missingLines = []
    dictionary = {}
    
    for ii in range(1, len(lines)):
        line = lines[ii]
        words = line.split(",")
        if len(words[2]) == 0: 
            missingLines.append(ii);
            continue
        value = dictionary.get(words[0], -1)
        if value == -1:
            dictionary[words[0]] = int(words[2])
        else: 
            if int(words[2]) < value: 
                dictionary[words[0]] = int(words[2])
    
    for ii in range(len(lines)):
        line = lines[ii]
        if ii in missingLines: 
            words = line.split(",")
            value = dictionary.get(words[0], 0)
            words[2] = str(value)
            line = ",".join(words)
            newFile.write(line)
        else: 
            newFile.write(line)
except: 
    print("Error has occured!")     
finally:
    file.close()
    newFile.close()
