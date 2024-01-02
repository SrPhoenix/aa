from collections import Counter
import os
import time
    
def get_letter_frequencies(text):
    # Convert text to lowercase and remove non-alphabetic characters
    cleaned_text = re.sub(r'[^a-z]', '', text.lower())
    
    # Count the frequency of each letter
    frequencies = Counter(cleaned_text)
    
    return frequencies

def calculate_probabilities(frequencies):
    # Sort letters by frequency in decreasing order
    sorted_letters = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    # Assign probability counter using the formula 1/2^k
    probabilities = {letter: 1 / (2 ** (i + 1)) for i, (letter, _) in enumerate(sorted_letters)}
    
    return probabilities


def main():
    # Read text from a file
    with open('your_text_file.txt', 'r') as file:
        text = file.read()

    # Get letter frequencies
    frequencies = get_letter_frequencies(text)

    # Calculate probabilities based on decreasing frequency
    probabilities = calculate_probabilities(frequencies)

    # Display letters and their probabilities
    for letter, probability in probabilities.items():
        print(f"{letter}: {probability}")

if __name__ == "__main__":
    main()