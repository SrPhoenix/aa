from collections import defaultdict
import os
import time
from  preprocess_file import process_file
import json


class SpaceSavingCounter:
    def __init__(self, k):
        self.k = k
        self.counts = defaultdict(int)

    def process_character(self, char):
        if char in self.counts:
            self.counts[char] += 1
        elif len(self.counts) < self.k - 1:
            self.counts[char] = 1
        else:
            # Decrease count for all existing keys, remove if count becomes 0
            for key in list(self.counts.keys()):
                self.counts[key] -= 1
                if self.counts[key] == 0:
                    del self.counts[key]

    def process_file(self,processedFile):

        startingTime = time.time()

        for char in processedFile:
            self.process_character(char)

        processingTimer = time.time() - startingTime

        return sorted(self.counts.items(), key=lambda item: item[1], reverse=True), processingTimer

if __name__ == "__main__":
    # Set all possible k
    all_k = [3, 5, 10]

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

        for k in all_k:

            space_saving_counter = SpaceSavingCounter(k)

            # get approximate counters
            result, processingTimer = space_saving_counter.process_file(processedFile)

            # store the counters
            results.write(json.dumps(result) + "\n")

            analysis.write(f'{"title":<40} {"K": 5}{"Processing Time" :<25}\n')

            # Store processing time
            analysis.write(f'{book + ":":<40} {k: 5} {processingTimer :<25}\n')

        analysis.close()
        results.close()
