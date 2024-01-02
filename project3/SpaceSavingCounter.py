from collections import defaultdict
import os
import time

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

    def process_file(self,file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            for char in text:
                self.process_character(char)

    def get_top_k(self):
        return sorted(self.counts.items(), key=lambda item: item[1], reverse=True)

if __name__ == "__main__":
    k = 5  
    space_saving_counter = SpaceSavingCounter(k)
    folder_path = "processed"
    path_files = [f for f in os.listdir(folder_path) if os.path.isfile( os.path.join(folder_path, f)) ]
    languages = {}
    for file in path_files:
        analysis_file = open("analysis/SpaceSavingCounter/"+file[:-4]+".txt", "w", encoding="utf-8")    
        csv_file = open("csv/SpaceSavingCounter/"+file[:-4]+".csv", "w", encoding="utf-8")    
        analysis_file.write(f"{'letter':<8} {'Attemps':<15} {'Operations':<15} {'Time':<13}\n")
        csv_file.write(f"{'letter':<8} {'Attemps':<15} {'Operations':<15} {'Time':<13}\n")
        print(f"{'Book':<20} {'Attemps':<15} {'Operations':<15} {'Time':<13}\n")
        file_path = folder_path+"/"+file
        start = time.time()
        space_saving_counter.process_file(file_path)
        end = time.time()

        result = space_saving_counter.get_top_k()

        analysis_file.write(f"{file:<20} {os.stat(file_path).st_size / 1024:<12} {'Attemps':<15} {'Operations':<15} {end - start:.4f}\n")

        # print(f"The most frequent letters are:")
        language = file.split("Book")[0]
        print(language)
        if language in languages:
            languages[language][file] = result
        else:
            languages[language] = {file : result}
        # results_file.write(f"{letter}: {count} occurrences\n")
        analysis_file.close()

    # for language in languages.keys():
    #     results_file = open("results/"+language+".txt", "w")
    #     for file in languages[language]:
    #         results_file.write(file+"\n")
    #         for letter, count in languages[language][file]:
    #             print(f"{letter}: {count} occurrences")
    #             results_file.write(f"{letter}: {count} occurrences\n")
    #         results_file.write("\n\n")
    #     results_file.close()
