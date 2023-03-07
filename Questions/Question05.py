import numpy as np
try: 
    file = open("imputed_country_vaccination_stats.csv", "r")
    lines = file.readlines()
    
    dictionary = {}
    
    for ii in range(1, len(lines)):
        line = lines[ii]
        words = line.split(",")
        valuesList = dictionary.get(words[0], -1)
        if valuesList == -1:
            dictionary[words[0]] = [int(words[2])]
        else: 
            valuesList.append(int(words[2]))
            
    mediansList = []
    
    for key, value in dictionary.items(): 
        
        newTuple = np.median(value), key
        mediansList.append(newTuple)
    
    mediansList.sort()
    mediansList.reverse()
    print("Top 3 Countries With Highest Median Daily Vaccination Numbers:\n1.%s \n2.%s\n3.%s\n"
          % (mediansList[0][1], mediansList[1][1], mediansList[2][1]))
except: 
    print("Error has occured!")     
finally:
    file.close()