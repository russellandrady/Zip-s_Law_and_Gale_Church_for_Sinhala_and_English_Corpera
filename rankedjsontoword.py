import json
from docx import Document
import os
from collections import defaultdict

# Read JSON file
with open('english_ranked_words.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Aggregate words by their counts
count_groups = defaultdict(list)
for word, count in data.items():
    count_groups[count].append(word)

# Sort counts in descending order
sorted_counts = sorted(count_groups.items(), key=lambda x: x[0], reverse=True)

# Create a Word document
doc = Document()

# Determine the table size
rows = len(sorted_counts) + 1  # +1 for the header row
cols = 3  # We have three columns: 'Rank', 'Count', and 'Words'

# Add a table with the appropriate number of rows and columns
table = doc.add_table(rows=rows, cols=cols)

# Add the header row (for 'Rank', 'Count', and 'Words')
header = table.rows[0].cells
header[0].text = 'Rank'
header[1].text = 'Count'
header[2].text = 'Words'

# Add data rows with ranks
for rank, (count, words) in enumerate(sorted_counts, start=1):
    row = table.rows[rank].cells
    row[0].text = str(rank)  # First column: Rank
    row[1].text = str(count)  # Second column: Count
    row[2].text = ', '.join(words)  # Third column: Words, joined by commas

# Save the document. If it exists, it will be overwritten
word_output_file = 'output_english_ranked_words.docx'
if os.path.exists(word_output_file):
    os.remove(word_output_file)

doc.save(word_output_file)

print("Word document created: output_english_ranked_words.docx")

# Save data as JSON
json_output_file = 'output_english_ranked_words.json'
ranked_data = [{"Rank": rank, "Count": count, "Words": words} for rank, (count, words) in enumerate(sorted_counts, start=1)]

with open(json_output_file, 'w', encoding='utf-8') as json_file:
    json.dump(ranked_data, json_file, ensure_ascii=False, indent=4)

print(f"JSON file created: {json_output_file}")
