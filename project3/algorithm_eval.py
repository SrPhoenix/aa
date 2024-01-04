import json
import numpy as np


def decreasing_probability_counter_analysis(title, exact_counter_result):

    # Total number of letters
    total_num_letters = []

    # Dictionary with the total number of occurrences of each letter
    occurances_per_letter = {}

    # store the sequence of occurence of each letter in each trial
    sequence_safe = {}

    # Get the top 3 most occurred letters
    top_3_letters = {}

    # Store the most occured letter in each trial
    all_most_occured_letter = {}

    with open("results/DecreasingProbabilityCounter/" + title + ".txt", "r", encoding="utf8") as file:

        while True:

            line = file.readline()

            if not line:
                break

            results = dict(json.loads(line))
            results = dict(sorted(results.items(), key=lambda l: l[1], reverse=True))

            # get total number of letters
            total = sum(results.values())
            total_num_letters.append(total)

            # Obtain results
            for letter, count in results.items():

                if letter not in occurances_per_letter:
                    occurances_per_letter[letter] = []

                occurances_per_letter[letter].append(count)

            # Store letters Occurrence sequence
            sequence = "".join(results)
            if sequence not in sequence_safe:
                sequence_safe[sequence] = 0

            sequence_safe[sequence] += 1

            # Get the 3 most occurred letter
            sequence = sequence[:3]

            if sequence not in top_3_letters:
                top_3_letters[sequence] = 0

            top_3_letters[sequence] += 1

            # Obtain most frequent letter
            most_occured_letter = sequence[0]

            if most_occured_letter not in all_most_occured_letter:
                all_most_occured_letter[most_occured_letter] = 0

            all_most_occured_letter[most_occured_letter] += 1

    # Keep track of mean counter values
    avg_counts = {letter: sum(count)/len(count) for letter, count in occurances_per_letter.items()}
    avg_counts = dict(sorted(avg_counts.items(), key=lambda l: l[1], reverse=True))

    real_sequence = "".join(exact_counter_result.keys())

    # Decreasing probability counter : 1 / 2^k
    # n_events = 2**k – 1  =>
    # => k = log_2(n_events  +  1) =>
    # => k = log(n_events + 1)/log(2)

    # Expected value of each counter
    expected_value_dict = {letter: np.log(count + 1) / np.log(2)
                           for letter, count in exact_counter_result.items()}

    # Expected value
    expected_value = sum(expected_value_dict.values())

    # Real value
    real_value = sum(exact_counter_result.values())

    # Calculate errors
    real_variance, real_standard_deviation, mean_absolute_error, mean_relative_error, mean_accuracy_ratio, \
        smallest_value, largest_value, mean, mean_absolute_deviation, standard_deviation, maximum_deviation, \
        variance = calculate_absolute_and_relative_errors(real_value, total_num_letters, expected_value)

    # Sequences sorted by frequency
    sequence_safe = {letter: counter for letter, counter in sorted(sequence_safe.items(),
                                                                  key=lambda l: l[1], reverse=True)}

    # Expected value of each counter sorted by frequency
    expected_value_dict = {letter: counter for letter, counter in sorted(expected_value_dict.items(),
                                                                         key=lambda l: l[1], reverse=True)}

    # First 3 letters sorted by frequency
    top_3_letters = {letter: counter for letter, counter in sorted(top_3_letters.items(),
                                                                     key=lambda l: l[1], reverse=True)}

    # Most frequent letters sorted by frequency
    all_most_occured_letter = {letter: counter for letter, counter in sorted(all_most_occured_letter.items(),
                                                                           key=lambda l: l[1], reverse=True)}

    # Sequence Accuracy
    sequence_accuracy = sequence_safe[real_sequence] / sum(sequence_safe.values()) if real_sequence in sequence_safe else 0

    # First 3 letters Accuracy
    first_3_letters_accuracy = top_3_letters[real_sequence[:3]] / sum(top_3_letters.values()) if real_sequence[:3] in top_3_letters else 0

    with open("evalAlgorithm/DecreasingProbabilityCounter/" + title + ".txt", "w", encoding="utf8") as stats:



        stats.write(f"Largest counter value: {largest_value}\n\n")
        stats.write(f"Smallest counter value: {smallest_value}\n")

        stats.write(f"Expected value: {expected_value}\n")
        stats.write(f"Variance: {real_variance}\n")
        stats.write(f"Standard deviation: {real_standard_deviation}\n\n")


        stats.write(f"Mean counter value: {mean}\n")
        stats.write(f"Mean absolute deviation: {mean_absolute_deviation}\n")
        stats.write(f"Standard deviation: {standard_deviation}\n")
        stats.write(f"Maximum deviation: {maximum_deviation}\n")
        stats.write(f"Variance: {variance}\n\n")


        stats.write(f"Mean absolute error: {mean_absolute_error}\n")
        stats.write(f"Mean relative error: {mean_relative_error * 100}%\n")
        stats.write(f"Mean accuracy ratio: {mean_accuracy_ratio * 100}%\n\n")

        stats.write(f"Real Char Frequency Sequence: {real_sequence}\n")
        stats.write(f"Letter Sequence Accuracy: {sequence_accuracy * 100}%\n")
        stats.write("5 Most Common Sequences:\n")


        for i, sequence in enumerate(sequence_safe):
            if i >= 5:
                break
            stats.write(f'{sequence}: {sequence_safe[sequence]}\n')

        stats.write("\n")

        stats.write(f'Top 3 Char Sequence Accuracy: {first_3_letters_accuracy * 100}%\n')
        stats.write('5 Most Common Sequences:\n')
        for i, sequence in enumerate(top_3_letters):
            if i >= 5:
                break
            stats.write(f'{sequence}: {top_3_letters[sequence]}\n')

        stats.write("\n")

        stats.write('Mean Counter Values per letter:\n')
        stats.write(f'Letter : Counter Value : Expected Value\n')
        for letter, counter in avg_counts.items():
            stats.write(f'{letter:<8} : {counter:<14} : {expected_value_dict[letter]}\n')

        stats.write("\n")


def calculate_absolute_and_relative_errors(real_value, counters, expected_value):

    # Real Variance
    real_variance = expected_value / 2

    # Real standard deviation
    real_standard_deviation = np.sqrt(real_variance)

    # -----------------------------

    n = len(counters)
    mean = sum(counters) / n

    # Maximum deviation
    maximum_deviation = max([abs(total - mean) for total in counters])

    # Mean absolute deviation
    mean_absolute_deviation = sum([abs(total - mean) for total in counters]) / n

    # Variance
    variance = sum([(count - mean) ** 2 for count in counters]) / n

    # Standard deviation (variance ** 0.5)
    standard_deviation = np.sqrt(sum([(count - mean) ** 2 for count in counters]) / n)

    # Mean absolute error
    mean_absolute_error = sum([abs(count - real_value) for count in counters]) / n

    # Mean relative error
    mean_relative_error = sum([abs(count - real_value) / real_value * 100 for count in counters]) / n

    # Mean accuracy ratio
    # mean_accuracy_ratio = len([total for total in total_letters if total == real_total]) / n
    mean_accuracy_ratio = mean / expected_value

    # -----------------------------

    # Smallest counter value
    smallest_value = min(counters)

    # Largest counter value
    largest_value = max(counters)

    return real_variance, real_standard_deviation, mean_absolute_error, mean_relative_error, mean_accuracy_ratio, \
        smallest_value, largest_value, mean, mean_absolute_deviation, standard_deviation, maximum_deviation, variance




def get_exact_counter_result(title):
    print("title",title)
    with open("results/exactCounter/" + title + ".txt", "r", encoding="utf8") as result:
        line = result.readline()

        occurances_per_letter = dict(json.loads(line))

        return dict(sorted(occurances_per_letter.items(), key=lambda l: l[1], reverse=True))



def compare_data_stream_counters(title, exact_counters):

    # Set all possible k
    all_k = [3, 5, 10]

    with open("results/SpaceSavingCounter/" + title + ".txt", "r", encoding="utf8") as file:
        results = file.readlines()

    for i in range(len(all_k)):
        k = all_k[i]

        counters = dict(json.loads(results[i]))

        top_k_letters = sorted(exact_counters.items(), key=lambda x: x[1], reverse=True)[:k-1]

        with open("evalAlgorithm/SpaceSavingCounter/" + title + "_K_" + str(k) + ".txt", "w", encoding="utf8") as stats:

            stats.write(f"Top {k-1} letters (Exact Counter):\n")
            for letter, counter in top_k_letters:
                stats.write(f"{letter}: {counter}\n")
            
            stats.write(f"\nTop {k-1} letters (Space Saving Counter):\n")
            for letter, counter in counters.items():
                stats.write(f"{letter}: {counter}\n")
                
            # Accurate letters
            accurate_letters = len([letter for letter, counter in top_k_letters if letter in counters])

            # Accuracy
            accuracy = accurate_letters/(k-1)

            stats.write(f"\nAccurate letters: {accurate_letters}/{k-1}\n")
            stats.write(f"Accuracy: {accuracy * 100}%\n")

if __name__ == "__main__":

    # Title o the titles 
    pathFiles = ["Das Bildnis des Dorian Gray", "Dorian Grayn muotokuva", "Het portret van Dorian Gray", "Le portrait de Dorian Gray","The Picture of Dorian Gray"] 

    for title in pathFiles:

        exact_counter_result = get_exact_counter_result(title)

        # Do the computational analysis of the decreasing probability counter algorithm
        decreasing_probability_counter_analysis(title, exact_counter_result)

        # Do the computational analysis of the space saving counter algorithm
        compare_data_stream_counters(title, exact_counter_result)