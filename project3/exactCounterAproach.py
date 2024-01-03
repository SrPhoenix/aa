from collections import Counter
import os
import time
from  preprocess_file import process_file


def most_frequent_letters_identifier(processedFile):
    # Count occurrences of each letter
    letter_counts = Counter(c for c in processedFile)

    # Return the most frequent letters
    return sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

if __name__ == "__main__":
    # Title o the books 
    pathFiles = ["Das Bildnis des Dorian Gray", "Dorian Grayn muotokuva", "Het portret van Dorian Gray", "Le portrait de Dorian Gray","The Picture of Dorian Gray"] 

    # Language o the books 
    languages = ["german", "finnish","dutch","french","english"]
    for i in range(len(pathFiles)):
        book = pathFiles[i][:-4]
        print(book)
        processedFile = process_file(pathFiles[i],languages[i])
        analysis_file = open("analysis/exactCounter/"+book+ ".txt", "w", encoding="utf-8")    

        start = time.time()
        result = most_frequent_letters_identifier(processedFile)
        end = time.time()
        
        analysis_file.write(f"Time: {end - start:.4f} \n\n")

        print(f"Time: {end - start:.4f}\n")

        analysis_file.write(f"{'letter':<8} {'Ocurrences':<12} \n")
        print(f"{'letter':<8} {'Ocurrences':<12}")

        for letter, occurences in result:
            print(f"{letter:<8} {occurences:<12}")
            analysis_file.write(f"{letter:<8} {occurences:<12}\n")



