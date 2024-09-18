import json
from docx import Document
import os

# Read JSON file
with open('preprocessed_sentences.json','r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Create a Word document
doc = Document()

# Determine the table size
rows = len(data) + 1  # +1 for the header row
cols = len(data[0])

# Add a table
table = doc.add_table(rows=rows, cols=cols)

# Add header row
header = table.rows[0].cells
for i, key in enumerate(data[0].keys()):
    header[i].text = key

# Add data rows
for i, item in enumerate(data):
    row = table.rows[i+1].cells
    for j, value in enumerate(item.values()):
        row[j].text = str(value)

# Save the document. if it exists, it will be overwritten

if os.path.exists('output_preprocessed_sentences.docx'):
    os.remove('output_preprocessed_sentences.docx')

doc.save('output_preprocessed_sentences.docx')
