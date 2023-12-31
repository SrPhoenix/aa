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
    filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuation]
    return ' '.join(filtered_words)

def remove_stopwords_and_punctuation_from_file(input_file, output_file, language):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        processed_text = remove_stopwords_and_punctuation(text,language)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_text.upper())


if __name__ == "__main__":
    folder_path = "books"
    output_folder = "processed"
    path_files = [f for f in os.listdir(folder_path) if os.path.isfile( os.path.join(folder_path, f)) ]
    languages = {}
    for file in path_files:
        file_path = folder_path+"/"+file
        output_path  = output_folder+"/"+file
        print(f"{file}")
        language = file.split("Book")[0]
        # with open(file_path, 'r', encoding='utf-8') as file:
        #     text = file.read()
        remove_stopwords_and_punctuation_from_file(file_path,output_path,language.lower()) 
    
