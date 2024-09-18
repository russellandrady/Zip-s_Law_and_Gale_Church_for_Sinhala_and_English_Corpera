import json
from docx import Document
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Paths to the JSON files
english_words_json = 'english_ranked_words.json'
output_english_ranked_json = 'output_english_ranked_words.json'
sinhala_words_json = 'sinhala_ranked_words.json'
output_sinhala_ranked_json = 'output_sinhala_ranked_words.json'

# Paths for the output Word documents and plots
output_english_doc = 'output_english_top_25.docx'
output_sinhala_doc = 'output_sinhala_top_25.docx'
english_plot = 'english_rank_vs_freq_product.png'
sinhala_plot = 'sinhala_rank_vs_freq_product.png'

# Set Bhashitha font for Sinhala text
bhashitha_font_path = './Bhashita.ttf'  # Path to the font in your project folder
sinhala_font_prop = fm.FontProperties(fname=bhashitha_font_path)

def create_word_document(top_words, output_json_file, output_doc, font_prop=None):
    # Read the output JSON file
    with open(output_json_file, 'r', encoding='utf-8') as file:
        output_data = json.load(file)

    # Create a dictionary from the output JSON for quick lookup
    output_dict = {}
    for entry in output_data:
        for word in entry['Words']:
            output_dict[word] = entry

    # Create a Word document
    doc = Document()

    # Add a table with columns: 'Word', 'Rank', 'Count', and 'Frequency * Rank'
    table = doc.add_table(rows=len(top_words) + 1, cols=4)  # +1 for header row

    # Add the header row
    header = table.rows[0].cells
    header[0].text = 'Word'
    header[1].text = 'Rank'
    header[2].text = 'Count'
    header[3].text = 'Frequency * Rank'

    # Add data rows with rank and frequency for top words
    words = []
    ranks = []
    counts = []
    freq_rank_products = []

    for word in top_words:
        if word in output_dict:
            rank = output_dict[word]['Rank']
            count = output_dict[word]['Count']
            freq_rank_product = count * rank
        else:
            rank = count = freq_rank_product = 'Not Found'

        # Add row to the table
        row = table.add_row().cells
        row[0].text = word
        row[1].text = str(rank)
        row[2].text = str(count)
        row[3].text = str(freq_rank_product)
        
        # Collect data for plotting
        if rank != 'Not Found':
            words.append(word)
            ranks.append(rank)
            counts.append(count)
            freq_rank_products.append(freq_rank_product)

    # Save the document. If it exists, it will be overwritten
    if os.path.exists(output_doc):
        os.remove(output_doc)

    doc.save(output_doc)

    # Plot for rank vs frequency product
    plt.figure(figsize=(10, 6))
    plt.bar(words, freq_rank_products, color='skyblue')
    plt.xlabel('Words', fontproperties=font_prop)
    plt.ylabel('Frequency * Rank', fontproperties=font_prop)
    plt.title('Rank vs Frequency * Rank')
    plt.xticks(rotation=90, fontproperties=font_prop)
    plt.tight_layout()
    plt.show()
    plt.close()

    print(f"Word document created: {output_doc}")


# Process English words
with open(english_words_json, 'r', encoding='utf-8') as file:
    english_words_data = json.load(file)

# Sort words by frequency in descending order and limit to the top 25
sorted_english_words = sorted(english_words_data.items(), key=lambda x: x[1], reverse=True)
top_25_english_words = [word for word, count in sorted_english_words[:25]]

# Generate Word document and plot for English
create_word_document(top_25_english_words, output_english_ranked_json, output_english_doc)

# Process Sinhala words
with open(sinhala_words_json, 'r', encoding='utf-8') as file:
    sinhala_words_data = json.load(file)

# Sort words by frequency in descending order and limit to the top 25
sorted_sinhala_words = sorted(sinhala_words_data.items(), key=lambda x: x[1], reverse=True)
top_25_sinhala_words = [word for word, count in sorted_sinhala_words[:25]]

# Generate Word document and plot for Sinhala
create_word_document(top_25_sinhala_words, output_sinhala_ranked_json, output_sinhala_doc, font_prop=sinhala_font_prop)
