import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import json
from collections import Counter

# Load the preprocessed JSON file
with open('preprocessed_sentences.json', 'r', encoding='utf-8') as file:
    preprocessed_data = json.load(file)

# Collect all words in Sinhala and English corpora
sinhala_words = []
english_words = []

for pair in preprocessed_data:
    sinhala_words.extend(pair['Sinhala'])
    english_words.extend(pair['English'])

# Calculate word frequencies using Counter
sinhala_word_freq = Counter(sinhala_words)
english_word_freq = Counter(english_words)

# Sort words by frequency in descending order
sorted_sinhala_freq = sorted(sinhala_word_freq.items(), key=lambda x: x[1], reverse=True)
sorted_english_freq = sorted(english_word_freq.items(), key=lambda x: x[1], reverse=True)

# Get the top 100 most frequent words in Sinhala and English for visualization
top_100_sinhala = sorted_sinhala_freq[:100]
top_100_english = sorted_english_freq[:100]

# Set Bhashitha font for Sinhala text
bhashitha_font_path = './Bhashita.ttf'  # Path to the font in your project folder
sinhala_font_prop = fm.FontProperties(fname=bhashitha_font_path)

# Function to plot word frequencies with words on the x-axis and frequencies on the y-axis
def plot_word_frequencies(word_freq, language, font_prop=None):
    words, freqs = zip(*word_freq)
    
    plt.figure(figsize=(20, 8)) 
    
    plt.bar(words, freqs, color='skyblue')
    
    plt.ylabel('Frequency', fontsize=12, fontproperties=font_prop)
    plt.title(f'Top 100 Most Frequent Words in {language}', fontsize=14, fontproperties=font_prop)
    
    plt.xticks(rotation=90, fontsize=10, fontproperties=font_prop)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Plot the top 100 most frequent Sinhala words with Bhashitha font
plot_word_frequencies(top_100_sinhala, "Sinhala", font_prop=sinhala_font_prop)

# Plot the top 100 most frequent English words with default font
plot_word_frequencies(top_100_english, "English")
