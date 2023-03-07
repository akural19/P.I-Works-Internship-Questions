import numpy as np
import re

regex = "[/][{1}[a-zA-Z0-9_.]+[<]{1}"

try: 
    file = open("URLdataset.csv", "r")
    newFile = open("manipulatedURLdataset.csv", "w")
    lines = file.readlines()
    
    for ii in range(1, len(lines)): 
        words = lines[ii].split(",")
        words[1] = re.search(regex, words[1]).group().lstrip("/").rstrip("<")
        newFile.write(",".join(words) + "\n")
except: 
    print("Error has occured!")     
finally:
    file.close()
    newFile.close()