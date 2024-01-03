from collections import Counter
import os
import time
import numpy as np
from  preprocess_file import process_file
import json


def approximate_counter(processedFile):

    startingTime = time.time()

    counter = {}

    for letter in processedFile:

        if letter not in counter:
            counter[letter] = 0

        # Counter has value k
        k = counter[letter]

        # Decreasing probability counter : 1 / 2^k
        probability = 1 / (2 ** k)

        # Increment with previous probability
        if np.random.uniform(0, 1) <= probability:
            counter[letter] += 1

    processingTimer = time.time() - startingTime

    return counter, processingTimer


if __name__ == "__main__":
    # Number of trials
    numTrials = 10000

    # Set seed with nMec
    np.random.seed(98515)
    # folder_path = "processed"
    
    # Title o the books 
    pathFiles = ["Das Bildnis des Dorian Gray", "Dorian Grayn muotokuva", "Het portret van Dorian Gray", "Le portrait de Dorian Gray","The Picture of Dorian Gray"] 

    # Language o the books 
    languages = ["german", "finnish","dutch","french","english"]

    for i in range(pathFiles):
        book = pathFiles[i]
        processedFile = process_file(pathFiles[i],languages[i])

        results = open("results/DecreasingProbabilityCounter/" + book + ".txt", "w", encoding="utf-8")
        analysis = open("analysis/DecreasingProbabilityCounter/" + book + ".txt", "w", encoding="utf-8")
        avgTime = 0

        for trial in range(numTrials):

            # get approximate counters
            counter, processingTimer = approximate_counter(processedFile)

            # store the counters
            results.write(json.dumps(counter) + "\n")

            # Update the timer
            avgTime += processingTimer

        # Store average processing time
        analysis.write(f'{book + ":":<40} {avgTime / numTrials:<25}\n')

        analysis.close()
        results.close()