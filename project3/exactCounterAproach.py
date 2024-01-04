from collections import Counter
import os
import time
from  preprocess_file import process_file
import json


def most_frequent_letters_identifier(processedFile):
    # Count occurrences of each letter
    letter_counts = Counter(processedFile)

    return letter_counts

if __name__ == "__main__":
    # Title o the books 
    pathFiles = ["Das Bildnis des Dorian Gray", "Dorian Grayn muotokuva", "Het portret van Dorian Gray", "Le portrait de Dorian Gray","The Picture of Dorian Gray"] 

    # Language o the books 
    languages = ["german", "finnish","dutch","french","english"]
    for i in range(len(pathFiles)):
        book = pathFiles[i]
        print(book)
        processedFile = process_file(pathFiles[i],languages[i],"exactCounter")
        analysis = open("analysis/exactCounter/"+book+ ".txt", "w", encoding="utf-8")    
        results = open("results/exactCounter/"+book+ ".txt", "w", encoding="utf-8")    
        start = time.time()
        result = most_frequent_letters_identifier(processedFile)
        end = time.time()
        
        analysis.write(f"Time: {end - start:.4f} \n\n")

        print(f"Time: {end - start:.4f}\n")

        results.write(json.dumps(result) + "\n")



