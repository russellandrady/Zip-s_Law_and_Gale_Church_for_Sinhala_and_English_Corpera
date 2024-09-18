import nltk
import json
import re

nltk.download('punkt')

# Function to tokenize, clean Sinhala text
def tokenize_and_clean(text):
    tokens = nltk.word_tokenize(text)
    
    # Keep only Sinhala Unicode characters (removes punctuation and other characters)
    regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    tokens = [regex.sub('', word) for word in tokens]
    
    # Remove empty tokens
    tokens = [token for token in tokens if token]
    
    return tokens

# Function to preprocess English text (tokenization, lowercasing, and removing punctuation)
def preprocess_english(sentence):
    words = nltk.word_tokenize(sentence)
    words = [word.lower() for word in words if word.isalnum()]
    return words

# Load the JSON file with the parallel sentences
with open('sentences.json', 'r', encoding='utf-8') as file:
    sentences = json.load(file)

# Preprocess both Sinhala and English sentences
preprocessed_data = []
for pair in sentences:
    sinhala_words = tokenize_and_clean(pair['Sinhala_Sentence'])  # Tokenize and clean Sinhala text
    english_words = preprocess_english(pair['English_Sentence'])  # Tokenize and preprocess English text
    preprocessed_data.append({
        'Sinhala': sinhala_words,
        'English': english_words
    })

# Save the preprocessed data to a new JSON file
with open('preprocessed_sentences.json', 'w', encoding='utf-8') as outfile:
    json.dump(preprocessed_data, outfile, ensure_ascii=False, indent=4)

# Print confirmation
print("Preprocessed data saved to 'preprocessed_sentences.json'.")
