import numpy as np
try: 
    file = open("imputed_country_vaccination_stats.csv", "r")
    lines = file.readlines()
    
    sumOfVaccinations = 0
    
    for ii in range(1, len(lines)):
        line = lines[ii]
        words = line.split(",")
        if words[1] == "01/06/2021": 
             sumOfVaccinations += int(words[2])
    print("Sum of Vaccinations on '01/06/2021': %d" % sumOfVaccinations)
        
except: 
    print("Error has occured!")     
finally:
    file.close()