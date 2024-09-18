import json
from sklearn.metrics import accuracy_score

# Load original and re-aligned sentences
with open('sentences.json', 'r', encoding='utf-8') as f:
    original_pairs = json.load(f)

with open('re_aligned_sentences.json', 'r', encoding='utf-8') as f:
    re_aligned_pairs = json.load(f)

# Create dictionaries for easier lookup
original_dict = {pair['Sinhala_Sentence']: pair['English_Sentence'] for pair in original_pairs}
re_aligned_dict = {pair['Sinhala_Sentence']: pair['English_Sentence'] for pair in re_aligned_pairs}

# Prepare lists for accuracy calculation
y_true = []
y_pred = []

for sinhala_sentence in original_dict:
    if sinhala_sentence in re_aligned_dict:
        y_true.append(original_dict[sinhala_sentence])
        y_pred.append(re_aligned_dict[sinhala_sentence])
    else:
        y_true.append(original_dict[sinhala_sentence])
        y_pred.append(None)  # Assign None for missing alignments

# Calculate accuracy (excluding None values)
def calculate_accuracy(y_true, y_pred):
    # Filter out None values
    filtered_true = [t for t, p in zip(y_true, y_pred) if p is not None]
    filtered_pred = [p for p in y_pred if p is not None]

    if len(filtered_true) == 0:
        return 0

    return accuracy_score(filtered_true, filtered_pred)

# Compute accuracy
accuracy = calculate_accuracy(y_true, y_pred)

print(f'Accuracy of re-aligned sentences: {accuracy:.2f}')
