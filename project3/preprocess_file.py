import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os

nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords_and_punctuation(text, language):
    stop_words = set(stopwords.words(language)) #'english'
    punctuation = set(string.punctuation)
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.isalpha() and  word.lower() not in stop_words and word not in punctuation]
    return ' '.join(filtered_words)

def process_file(input_file,  language, folder_name):

    analysis_file = open("process/"+folder_name+"/"+input_file+".txt", "w", encoding="utf-8")    
    with open("books/"+input_file+".txt", 'r', encoding='utf-8') as file:
        text = file.read()
        
        # length of the text file before processing it
        initial_length = len(text)

        # Find header in the file
        header = f"*** START OF THE PROJECT GUTENBERG EBOOK {input_file.upper()} ***"
        start = text.find(header) + len(header)

        # Find footer in the file
        footer = f"*** END OF THE PROJECT GUTENBERG EBOOK {input_file.upper()} ***"
        end = text.find(footer)

        # Remove header and footer from the file
        text = text[start:end]

        processed_text = remove_stopwords_and_punctuation(text,language).upper()

        # Keep track of final length (after processing)
        final_length = len(text)

        # Store length of text before and after processing
        analysis_file.write(f'{input_file:<40} {initial_length:<25} {final_length}\n')
    
    return processed_text


