from collections import Counter
import os
import time


def most_frequent_letters_identifier(file_path, num_letters=5):
    operations_counter = 0
    attempts_counter = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.upper()

    # Count occurrences of each letter
    letter_counts = Counter(c for c in text if c.isalpha())

    # Return the most frequent letters
    most_common = letter_counts.most_common(num_letters)
    return most_common

if __name__ == "__main__":
    folder_path = "books"
    path_files = [f for f in os.listdir(folder_path) if os.path.isfile( os.path.join(folder_path, f)) ]
    languages = {}
    for file in path_files:
        results_file = open("results/results.txt", "w")    
        results_file.write(f"{'Book':<20} {'Size (kb)':<12} {'Attemps':<15} {'Operations':<15} {'Time':<13}\n")
        print(f"{'Book':<20} {'Size':<12} {'Attemps':<15} {'Operations':<15} {'Time':<13}\n")
        file_path = folder_path+"/"+file
        start = time.time()
        result = most_frequent_letters_identifier(file_path)
        end = time.time()

        results_file.write(f"{file:<20} {os.stat(file_path).st_size / 1024:<12} {'Attemps':<15} {'Operations':<15} {end - start:.4f}\n")

        # print(f"The most frequent letters are:")
        language = file.split("Book")[0]
        print(language)
        if language in languages:
            languages[language][file] = result
        else:
            languages[language] = {file : result}
        # results_file.write(f"{letter}: {count} occurrences\n")
        results_file.close()

    for language in languages.keys():
        results_file = open("results/"+language+".txt", "w")
        for file in languages[language]:
            results_file.write(file+"\n")
            for letter, count in languages[language][file]:
                print(f"{letter}: {count} occurrences")
                results_file.write(f"{letter}: {count} occurrences\n")
            results_file.write("\n\n")
        results_file.close()
