from collections import Counter
import os
import time


def most_frequent_letters_identifier(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Count occurrences of each letter
    letter_counts = Counter(c for c in text)

    # Return the most frequent letters
    # most_common = letter_counts.most_common(num_letters)
    return sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

if __name__ == "__main__":
    folder_path = "processed"
    path_files = [f for f in os.listdir(folder_path) if os.path.isfile( os.path.join(folder_path, f)) ]
    languages = {}
    for file in path_files:
        analysis_file = open("analysis/exactCounter/"+file[:-4]+".txt", "w", encoding="utf-8")    
        csv_file = open("csv/exactCounter/"+file[:-4]+".csv", "w", encoding="utf-8")    

        file_path = folder_path+"/"+file
        start = time.time()
        result = most_frequent_letters_identifier(file_path)
        end = time.time()
        analysis_file.write(f"Size (kb): {os.stat(file_path).st_size / 1024:<12} \n")
        analysis_file.write(f"Time: {end - start:.4f} \n\n")

        print(f"\nSize (kb): {os.stat(file_path).st_size / 1024:<12}")
        print(f"Time: {end - start:.4f}\n")

        analysis_file.write(f"{'letter':<8} {'Ocurrences':<12} \n")
        csv_file.write(f"{'letter':<8} {'Ocurrences':<12} \n")
        print(f"{'letter':<8} {'Ocurrences':<12}")

        for letter, occurences in result:
            print(f"{letter:<8} {occurences:<12}")
            analysis_file.write(f"{letter:<8} {occurences:<12}\n")
            csv_file.write(f"{letter:<8} {occurences:<12}\n")



